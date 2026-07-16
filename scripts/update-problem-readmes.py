#!/usr/bin/env python3
"""Download LeetCode questions and update every problem README with the full statement."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "lib"))

from html_to_markdown import leetcode_html_to_markdown, parse_hints  # noqa: E402
from doocs_fetcher import fetch_doocs_description  # noqa: E402

DOOCS_ATTRIBUTION = (
    "\n\n---\n"
    "_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) "
    "community mirror (LeetCode Premium)._"
)

DEFAULT_SOURCE = (
    "https://raw.githubusercontent.com/noworneverev/leetcode-api/main/data/leetcode_questions.json"
)


def folder_name(number: int, title_slug: str) -> str:
    return f"{number:04d}_{title_slug.replace('-', '_')}"


def extract_approach(existing_readme: str) -> str:
    match = re.search(r"## Approach\s*\n(.*)\Z", existing_readme, flags=re.DOTALL)
    if not match:
        return "<!-- Describe your solution approach here -->\n"

    approach = match.group(1).strip()
    if not approach:
        return "<!-- Describe your solution approach here -->\n"
    return approach + "\n"


def premium_problem_notice(leetcode_url: str) -> str:
    return (
        "> **LeetCode Premium** — No public mirror was found for this question. "
        f"View it on [LeetCode]({leetcode_url}) (Premium subscription required).\n\n"
        "If you have Premium, fetch it with your session cookie:\n\n"
        "```powershell\n"
        "$env:LEETCODE_SESSION = \"<your-session-cookie>\"\n"
        ".\\scripts\\update-problem-readmes.ps1 -FetchPremium\n"
        "```"
    )


def load_doocs_cache(cache_path: Path) -> dict[str, str]:
    if not cache_path.exists():
        return {}
    with cache_path.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def save_doocs_cache(cache_path: Path, cache: dict[str, str]) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with cache_path.open("w", encoding="utf-8") as handle:
        json.dump(cache, handle, ensure_ascii=False, indent=2)


def resolve_problem_markdown(
    question: dict,
    leetcode_url: str,
    *,
    doocs_cache: dict[str, str],
    include_doocs: bool,
    fetch_premium: bool,
    leetcode_session: str | None,
) -> tuple[str, bool]:
    """Return (problem markdown, doocs_cache_changed)."""
    number = int(question["questionFrontendId"])
    title = question["title"].strip()
    title_slug = question.get("url", "").rstrip("/").split("/")[-1]
    cache_key = str(number)
    cache_changed = False

    api_content = (question.get("content") or "").strip()
    if api_content:
        return leetcode_html_to_markdown(api_content), cache_changed

    if include_doocs:
        cached = doocs_cache.get(cache_key)
        if cached:
            return cached + DOOCS_ATTRIBUTION, cache_changed

        doocs_md = fetch_doocs_description(number, title)
        if doocs_md:
            body = doocs_md + DOOCS_ATTRIBUTION
            doocs_cache[cache_key] = body
            return body, True

    if fetch_premium and leetcode_session and question.get("isPaidOnly") and title_slug:
        fetched = fetch_premium_content(title_slug, leetcode_session)
        if fetched.strip():
            return leetcode_html_to_markdown(fetched), cache_changed

    if question.get("isPaidOnly"):
        return premium_problem_notice(leetcode_url), cache_changed

    return (
        "_Problem description unavailable in the cached LeetCode API data._ "
        "Try refreshing with `.\\scripts\\update-problem-readmes.ps1 -ForceRefresh`.",
        cache_changed,
    )


def fetch_premium_content(title_slug: str, session: str) -> str:
    query = {
        "query": """
        query questionContent($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            content
          }
        }
        """,
        "variables": {"titleSlug": title_slug},
        "operationName": "questionContent",
    }
    request = urllib.request.Request(
        "https://leetcode.com/graphql",
        data=json.dumps(query).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Cookie": f"LEETCODE_SESSION={session}",
            "User-Agent": "leetcode-solutions-readme-updater",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)

    question = (payload.get("data") or {}).get("question") or {}
    return question.get("content") or ""


def format_tags(question: dict) -> str:
    tags = question.get("topicTags")
    if isinstance(tags, list):
        slugs = []
        for item in tags:
            if not isinstance(item, dict):
                continue
            slug = item.get("slug") or item.get("name", "").lower().replace(" ", "-")
            if slug:
                slugs.append(slug)
        if slugs:
            return ", ".join(slugs)

    if isinstance(tags, str) and tags.strip():
        try:
            parsed = json.loads(tags)
            slugs = [item.get("slug", "") for item in parsed if item.get("slug")]
            if slugs:
                return ", ".join(slugs)
        except json.JSONDecodeError:
            cleaned = tags.strip()
            if cleaned:
                return cleaned
    return ""


def build_readme(
    question: dict,
    existing_readme: str | None,
    *,
    doocs_cache: dict[str, str],
    include_doocs: bool = True,
    fetch_premium: bool = False,
    leetcode_session: str | None = None,
) -> tuple[str, bool]:
    number = int(question["questionFrontendId"])
    title = question["title"]
    difficulty = question.get("difficulty", "Unknown")
    title_slug = question.get("url", "").rstrip("/").split("/")[-1]
    if not title_slug:
        title_slug = title.lower().replace(" ", "-")

    leetcode_url = question.get("url") or f"https://leetcode.com/problems/{title_slug}/"
    tags = format_tags(question)

    problem_md, cache_changed = resolve_problem_markdown(
        question,
        leetcode_url,
        doocs_cache=doocs_cache,
        include_doocs=include_doocs,
        fetch_premium=fetch_premium,
        leetcode_session=leetcode_session,
    )
    hints = parse_hints(question.get("hints"))

    lines = [
        f"# {number:04d}. {title}",
        "",
        f"- **Difficulty:** {difficulty}",
        f"- **LeetCode:** [{leetcode_url}]({leetcode_url})",
    ]
    if question.get("isPaidOnly"):
        lines.append("- **Premium:** Yes")
    if tags:
        lines.append(f"- **Tags:** {tags}")
    lines.extend(["", "## Problem", "", problem_md])

    if hints:
        lines.extend(["", "### Hints", ""])
        lines.extend(f"{index}. {hint}" for index, hint in enumerate(hints, start=1))

    lines.extend(["", "## Approach", ""])
    lines.append(extract_approach(existing_readme or ""))
    return "\n".join(lines).rstrip() + "\n", cache_changed


def load_questions(source_url: str, cache_path: Path, force_refresh: bool) -> list[dict]:
    if cache_path.exists() and not force_refresh:
        with cache_path.open(encoding="utf-8-sig") as handle:
            cached = json.load(handle)
        return [entry["data"]["question"] for entry in cached]

    with urllib.request.urlopen(source_url, timeout=180) as response:
        payload = json.load(response)

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with cache_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle)

    return [entry["data"]["question"] for entry in payload]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--source-url", default=DEFAULT_SOURCE)
    parser.add_argument("--force-refresh", action="store_true")
    parser.add_argument("--number", type=int, help="Update a single problem number")
    parser.add_argument(
        "--skip-doocs",
        action="store_true",
        help="Do not fetch Premium descriptions from doocs/leetcode mirror",
    )
    parser.add_argument(
        "--fetch-premium",
        action="store_true",
        help="Also try LeetCode GraphQL with LEETCODE_SESSION for remaining Premium gaps",
    )
    parser.add_argument(
        "--leetcode-session",
        default=None,
        help="LeetCode LEETCODE_SESSION cookie (or set LEETCODE_SESSION env var)",
    )
    args = parser.parse_args()

    leetcode_session = args.leetcode_session or os.environ.get("LEETCODE_SESSION")
    if args.fetch_premium and not leetcode_session:
        print("Error: --fetch-premium requires LEETCODE_SESSION (env var or --leetcode-session).")
        return 1

    repo_root = args.repo_root
    cache_path = repo_root / "config" / "questions-full.json"
    doocs_cache_path = repo_root / "config" / "doocs-premium-cache.json"
    questions = load_questions(args.source_url, cache_path, args.force_refresh)
    doocs_cache = load_doocs_cache(doocs_cache_path)
    include_doocs = not args.skip_doocs
    doocs_cache_changed = False

    if args.number is not None:
        questions = [q for q in questions if int(q["questionFrontendId"]) == args.number]

    updated = 0
    missing = 0
    doocs_fetched = 0

    for question in questions:
        number = int(question["questionFrontendId"])
        title_slug = question.get("url", "").rstrip("/").split("/")[-1]
        if not title_slug:
            continue

        target_dir = repo_root / folder_name(number, title_slug)
        readme_path = target_dir / "README.md"
        if not target_dir.exists():
            missing += 1
            continue

        existing = readme_path.read_text(encoding="utf-8-sig") if readme_path.exists() else ""
        readme_text, cache_changed = build_readme(
            question,
            existing,
            doocs_cache=doocs_cache,
            include_doocs=include_doocs,
            fetch_premium=args.fetch_premium,
            leetcode_session=leetcode_session,
        )
        if cache_changed:
            doocs_cache_changed = True
            doocs_fetched += 1
        readme_path.write_text(readme_text, encoding="utf-8")
        updated += 1

        if include_doocs and updated % 50 == 0 and doocs_cache_changed:
            save_doocs_cache(doocs_cache_path, doocs_cache)
            doocs_cache_changed = False

        if updated % 250 == 0 or updated == len(questions):
            print(f"Updated {updated} README files...")

    if include_doocs and doocs_cache_changed:
        save_doocs_cache(doocs_cache_path, doocs_cache)

    print(f"Done. Updated: {updated}, missing folders: {missing}, doocs fetched: {doocs_fetched}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
