"""Unofficial LeetCode.com client using session cookies (LEETCODE_SESSION + csrftoken)."""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

GRAPHQL_URL = "https://leetcode.com/graphql"
SITE_ORIGIN = "https://leetcode.com"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
REQUEST_DELAY_SECONDS = 0.35


@dataclass(frozen=True)
class LeetCodeCredentials:
    session: str
    csrf_token: str


@dataclass(frozen=True)
class SolvedQuestion:
    frontend_id: int
    title: str
    title_slug: str
    last_result: str


@dataclass(frozen=True)
class SubmissionOverview:
    submission_id: int
    lang_slug: str
    status_display: str


@dataclass(frozen=True)
class QuestionMeta:
    question_id: str
    frontend_id: int
    title: str
    title_slug: str
    sample_test_case: str


class LeetCodeError(Exception):
    pass


class LeetCodeClient:
    def __init__(
        self,
        credentials: LeetCodeCredentials,
        *,
        request_delay: float = REQUEST_DELAY_SECONDS,
    ) -> None:
        self.credentials = credentials
        self.request_delay = request_delay
        self._last_request_at = 0.0

    @classmethod
    def from_env(cls, repo_root: Path | None = None) -> LeetCodeClient:
        if repo_root is not None:
            load_dotenv_file(repo_root / ".leetcode.env")
            load_dotenv_file(repo_root / ".env")
        session = os.environ.get("LEETCODE_SESSION", "").strip()
        csrf = os.environ.get("LEETCODE_CSRF", os.environ.get("LEETCODE_CSRFTOKEN", "")).strip()
        if not session:
            raise LeetCodeError(
                "Missing LEETCODE_SESSION. Set it in the environment or in .leetcode.env "
                "(see .leetcode.env.example)."
            )
        if not csrf:
            raise LeetCodeError(
                "Missing LEETCODE_CSRF (or LEETCODE_CSRFTOKEN). Copy csrftoken from browser "
                "DevTools → Application → Cookies → leetcode.com."
            )
        return cls(LeetCodeCredentials(session=session, csrf_token=csrf))

    def _throttle(self) -> None:
        elapsed = time.monotonic() - self._last_request_at
        if elapsed < self.request_delay:
            time.sleep(self.request_delay - elapsed)

    def _headers(self, *, referer: str | None = None) -> dict[str, str]:
        referer = referer or f"{SITE_ORIGIN}/"
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Origin": SITE_ORIGIN,
            "Referer": referer,
            "User-Agent": USER_AGENT,
            "x-csrftoken": self.credentials.csrf_token,
            "Cookie": (
                f"LEETCODE_SESSION={self.credentials.session}; "
                f"csrftoken={self.credentials.csrf_token}"
            ),
        }

    def _request_json(
        self,
        url: str,
        *,
        method: str = "GET",
        payload: dict[str, Any] | None = None,
        referer: str | None = None,
    ) -> Any:
        self._throttle()
        data = None
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            url,
            data=data,
            headers=self._headers(referer=referer),
            method=method,
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                body = response.read()
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:500]
            raise LeetCodeError(f"HTTP {exc.code} for {url}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise LeetCodeError(f"Network error for {url}: {exc}") from exc
        finally:
            self._last_request_at = time.monotonic()

        if not body:
            return {}
        try:
            return json.loads(body)
        except json.JSONDecodeError as exc:
            preview = body[:300].decode("utf-8", errors="replace")
            raise LeetCodeError(f"Non-JSON response from {url}: {preview}") from exc

    def graphql(
        self,
        query: str,
        variables: dict[str, Any] | None = None,
        *,
        operation_name: str | None = None,
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {"query": query}
        if variables is not None:
            payload["variables"] = variables
        if operation_name:
            payload["operationName"] = operation_name
        result = self._request_json(GRAPHQL_URL, method="POST", payload=payload)
        if result.get("errors"):
            raise LeetCodeError(f"GraphQL error: {result['errors']}")
        return result.get("data") or {}

    def get_current_user(self) -> dict[str, Any]:
        data = self.graphql(
            """
            query globalData {
              userStatus {
                username
                isSignedIn
                isPremium
              }
            }
            """,
            operation_name="globalData",
        )
        user = data.get("userStatus") or {}
        if not user.get("isSignedIn"):
            raise LeetCodeError("Session cookie is invalid or expired.")
        return user

    def get_solved_questions(self, *, limit: int = 4000) -> list[SolvedQuestion]:
        data = self.graphql(
            """
            query userProgressQuestionList($filters: UserProgressQuestionListInput) {
              userProgressQuestionList(filters: $filters) {
                questions {
                  frontendId
                  title
                  titleSlug
                  questionStatus
                  lastResult
                }
              }
            }
            """,
            variables={
                "filters": {
                    "questionStatus": "SOLVED",
                    "skip": 0,
                    "limit": limit,
                }
            },
            operation_name="userProgressQuestionList",
        )
        questions = (data.get("userProgressQuestionList") or {}).get("questions") or []
        solved: list[SolvedQuestion] = []
        for item in questions:
            frontend_raw = item.get("frontendId")
            if frontend_raw is None:
                continue
            solved.append(
                SolvedQuestion(
                    frontend_id=int(frontend_raw),
                    title=str(item.get("title") or ""),
                    title_slug=str(item.get("titleSlug") or ""),
                    last_result=str(item.get("lastResult") or ""),
                )
            )
        return solved

    def get_latest_accepted_submission(
        self,
        title_slug: str,
        *,
        lang_slug: str | None = None,
    ) -> SubmissionOverview | None:
        variables: dict[str, Any] = {
            "questionSlug": title_slug,
            "offset": 0,
            "limit": 20 if lang_slug else 1,
            "lastKey": None,
            "status": 10,
        }
        if lang_slug is not None:
            variables["lang"] = lang_slug

        data = self.graphql(
            """
            query submissionList(
              $offset: Int!
              $limit: Int!
              $lastKey: String
              $questionSlug: String!
              $lang: Int
              $status: Int
            ) {
              questionSubmissionList(
                offset: $offset
                limit: $limit
                lastKey: $lastKey
                questionSlug: $questionSlug
                lang: $lang
                status: $status
              ) {
                submissions {
                  id
                  statusDisplay
                  lang
                }
              }
            }
            """,
            variables=variables,
            operation_name="submissionList",
        )
        submissions = (data.get("questionSubmissionList") or {}).get("submissions") or []
        if not submissions:
            return None

        if lang_slug is None:
            item = submissions[0]
        else:
            item = next((entry for entry in submissions if str(entry.get("lang") or "") == lang_slug), None)
            if item is None:
                return None

        return SubmissionOverview(
            submission_id=int(item["id"]),
            lang_slug=str(item.get("lang") or ""),
            status_display=str(item.get("statusDisplay") or ""),
        )

    def get_accepted_submissions_by_language(
        self,
        title_slug: str,
        *,
        limit: int = 100,
    ) -> dict[str, SubmissionOverview]:
        data = self.graphql(
            """
            query submissionList(
              $offset: Int!
              $limit: Int!
              $lastKey: String
              $questionSlug: String!
              $status: Int
            ) {
              questionSubmissionList(
                offset: $offset
                limit: $limit
                lastKey: $lastKey
                questionSlug: $questionSlug
                status: $status
              ) {
                submissions {
                  id
                  statusDisplay
                  lang
                }
              }
            }
            """,
            variables={
                "questionSlug": title_slug,
                "offset": 0,
                "limit": limit,
                "lastKey": None,
                "status": 10,
            },
            operation_name="submissionList",
        )
        submissions = (data.get("questionSubmissionList") or {}).get("submissions") or []
        by_lang: dict[str, SubmissionOverview] = {}
        for item in submissions:
            lang_key = str(item.get("lang") or "")
            if not lang_key or lang_key in by_lang:
                continue
            by_lang[lang_key] = SubmissionOverview(
                submission_id=int(item["id"]),
                lang_slug=lang_key,
                status_display=str(item.get("statusDisplay") or ""),
            )
        return by_lang

    def get_submission_code(self, submission_id: int) -> str:
        data = self.graphql(
            """
            query submissionDetails($submissionId: Int!) {
              submissionDetails(submissionId: $submissionId) {
                code
                lang {
                  name
                  verboseName
                }
              }
            }
            """,
            variables={"submissionId": submission_id},
            operation_name="submissionDetails",
        )
        details = data.get("submissionDetails") or {}
        code = details.get("code")
        if not code:
            raise LeetCodeError(f"No code returned for submission {submission_id}.")
        return str(code)

    def get_question(self, title_slug: str) -> QuestionMeta:
        data = self.graphql(
            """
            query questionData($titleSlug: String!) {
              question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                title
                titleSlug
                sampleTestCase
              }
            }
            """,
            variables={"titleSlug": title_slug},
            operation_name="questionData",
        )
        question = data.get("question")
        if not question:
            raise LeetCodeError(f"Question not found: {title_slug}")
        return QuestionMeta(
            question_id=str(question["questionId"]),
            frontend_id=int(question["questionFrontendId"]),
            title=str(question.get("title") or ""),
            title_slug=str(question.get("titleSlug") or title_slug),
            sample_test_case=str(question.get("sampleTestCase") or ""),
        )

    def submit_solution(
        self,
        title_slug: str,
        question_id: str,
        lang_slug: str,
        code: str,
    ) -> int:
        referer = f"{SITE_ORIGIN}/problems/{title_slug}/"
        payload = {
            "lang": lang_slug,
            "question_id": question_id,
            "typed_code": code,
            "test_mode": False,
            "judge_type": "large",
        }
        result = self._request_json(
            f"{SITE_ORIGIN}/problems/{title_slug}/submit/",
            method="POST",
            payload=payload,
            referer=referer,
        )
        submission_id = result.get("submission_id")
        if submission_id is None:
            raise LeetCodeError(f"Submit failed for {title_slug}: {result}")
        return int(submission_id)

    def run_solution(
        self,
        title_slug: str,
        question_id: str,
        lang_slug: str,
        code: str,
        *,
        data_input: str,
    ) -> str:
        referer = f"{SITE_ORIGIN}/problems/{title_slug}/"
        payload = {
            "lang": lang_slug,
            "question_id": question_id,
            "typed_code": code,
            "data_input": data_input,
            "test_mode": False,
        }
        result = self._request_json(
            f"{SITE_ORIGIN}/problems/{title_slug}/interpret_solution/",
            method="POST",
            payload=payload,
            referer=referer,
        )
        interpret_id = result.get("interpret_id") or result.get("interpret_expected_id")
        if interpret_id is None:
            raise LeetCodeError(f"Run failed for {title_slug}: {result}")
        return str(interpret_id)

    def poll_submission(self, submission_id: int | str, *, timeout: float = 120.0) -> dict[str, Any]:
        url = f"{SITE_ORIGIN}/submissions/detail/{submission_id}/check/"
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            result = self._request_json(url, method="GET")
            state = result.get("state")
            if state == "SUCCESS":
                return result
            if state not in (None, "PENDING", "STARTED"):
                return result
            time.sleep(2.0)
        raise LeetCodeError(f"Timed out waiting for submission {submission_id}.")


def load_dotenv_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def load_language_maps(repo_root: Path) -> tuple[dict[str, dict[str, str]], dict[str, str], dict[str, str]]:
    languages_path = repo_root / "config" / "languages.json"
    with languages_path.open(encoding="utf-8") as handle:
        languages = json.load(handle)

    by_id = {item["id"]: item for item in languages}
    leetcode_to_repo: dict[str, str] = {}
    repo_to_leetcode: dict[str, str] = {}
    for item in languages:
        repo_to_leetcode[item["id"]] = item["leetcodeSlug"]
        leetcode_to_repo[item["leetcodeSlug"]] = item["id"]

    extras = {
        "python": "python",
        "python3": "python",
        "golang": "go",
        "go": "go",
        "c++": "cpp",
        "c#": "csharp",
        "csharp": "csharp",
        "javascript": "javascript",
        "typescript": "typescript",
        "java": "java",
        "c": "c",
        "ruby": "ruby",
        "swift": "swift",
        "kotlin": "kotlin",
        "rust": "rust",
        "scala": "scala",
        "php": "php",
        "python3": "python",
        "Python3": "python",
        "Python": "python",
        "Java": "java",
        "C++": "cpp",
        "C": "c",
        "Go": "go",
        "Rust": "rust",
        "Kotlin": "kotlin",
        "Swift": "swift",
        "Ruby": "ruby",
        "C#": "csharp",
        "Scala": "scala",
        "PHP": "php",
        "JavaScript": "javascript",
        "TypeScript": "typescript",
    }
    for slug, repo_id in extras.items():
        leetcode_to_repo.setdefault(slug, repo_id)

    return by_id, leetcode_to_repo, repo_to_leetcode


def folder_name(number: int, title_slug: str) -> str:
    return f"{number:04d}_{title_slug.replace('-', '_')}"


def find_folder(repo_root: Path, *, number: int | None = None, folder: str | None = None) -> Path:
    if folder:
        path = repo_root / folder
        if not path.is_dir():
            raise LeetCodeError(f"Folder not found: {folder}")
        return path
    if number is None:
        raise LeetCodeError("Provide --folder or --number.")
    matches = sorted(repo_root.glob(f"{number:04d}_*"))
    if not matches:
        raise LeetCodeError(f"No folder found for problem number {number}.")
    if len(matches) > 1:
        raise LeetCodeError(f"Multiple folders match number {number}: {[p.name for p in matches]}")
    return matches[0]


def parse_folder_name(folder: str) -> tuple[int, str]:
    prefix, _, slug = folder.partition("_")
    if not prefix.isdigit() or not slug:
        raise LeetCodeError(f"Invalid folder name: {folder}")
    return int(prefix), slug.replace("_", "-")


def solution_header(number: int, title: str, title_slug: str, comment: str) -> str:
    padded = f"{number:04d}"
    return (
        f"{comment} LeetCode {padded} - {title}\n"
        f"{comment} https://leetcode.com/problems/{title_slug}/\n\n"
    )


def strip_solution_header(code: str) -> str:
    lines = code.splitlines()
    if not lines:
        return code
    first = lines[0].lstrip()
    if not (first.startswith("#") or first.startswith("//")):
        return code.lstrip("\n")

    body_start = 0
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            body_start = index + 1
            break
    if body_start == 0:
        for index, line in enumerate(lines):
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and not stripped.startswith("//"):
                body_start = index
                break
    return "\n".join(lines[body_start:]).lstrip("\n") + ("\n" if code.endswith("\n") else "")


def read_solution_file(path: Path) -> str:
    if not path.exists():
        raise LeetCodeError(f"Solution file not found: {path}")
    return strip_solution_header(path.read_text(encoding="utf-8"))


def write_solution_file(
    path: Path,
    code: str,
    *,
    number: int,
    title: str,
    title_slug: str,
    comment: str,
) -> None:
    header = solution_header(number, title, title_slug, comment)
    content = header + code.rstrip() + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
