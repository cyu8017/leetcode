#!/usr/bin/env python3
"""Submit or run a local solution on LeetCode using your session cookies."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "lib"))

from leetcode_api import (  # noqa: E402
    LeetCodeClient,
    LeetCodeError,
    find_folder,
    load_language_maps,
    parse_folder_name,
    read_solution_file,
)


def run_local_tests(repo_root: Path, folder: str, language: str) -> None:
    test_script = repo_root / "scripts" / "test.ps1"
    if not test_script.exists():
        raise LeetCodeError("Local test script not found: scripts/test.ps1")
    command = [
        "powershell",
        "-NoProfile",
        "-File",
        str(test_script),
        "-Folder",
        folder,
        "-Language",
        language,
        "-Local",
    ]
    print(f"Running local tests: {' '.join(command)}")
    completed = subprocess.run(command, cwd=repo_root)
    if completed.returncode != 0:
        raise LeetCodeError("Local tests failed. Fix the solution or pass --skip-local-test.")


def format_result(result: dict) -> str:
    status = result.get("status_msg") or result.get("state") or "Unknown"
    runtime = result.get("status_runtime") or result.get("runtime") or "?"
    memory = result.get("status_memory") or result.get("memory") or "?"
    passed = result.get("total_correct")
    total = result.get("total_testcases")
    testcase = result.get("last_testcase") or ""
    lines = [f"Status: {status}", f"Runtime: {runtime}", f"Memory: {memory}"]
    if passed is not None and total is not None:
        lines.append(f"Test cases: {passed}/{total}")
    if testcase:
        lines.append(f"Last testcase: {testcase}")
    for key in ("compile_error", "runtime_error", "full_compile_error"):
        value = result.get(key)
        if value:
            lines.append(f"{key}: {value}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=SCRIPT_DIR.parent.parent)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--folder", help="Problem folder, e.g. 0001_two_sum")
    group.add_argument("--number", type=int, help="Problem number, e.g. 1")
    parser.add_argument("--language", required=True, help="Repo language id, e.g. python")
    parser.add_argument("--run-only", action="store_true", help="Run on LeetCode examples (no submit)")
    parser.add_argument("--test-local", action="store_true", help="Run local tests before submit/run")
    parser.add_argument("--timeout", type=float, default=120.0, help="Submission poll timeout seconds")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    try:
        client = LeetCodeClient.from_env(repo_root)
        user = client.get_current_user()
        print(f"Signed in as {user.get('username')}")

        language_by_id, _, repo_to_leetcode = load_language_maps(repo_root)
        if args.language not in language_by_id:
            raise LeetCodeError(f"Unknown language id: {args.language}")

        problem_dir = find_folder(repo_root, number=args.number, folder=args.folder)
        _, title_slug = parse_folder_name(problem_dir.name)
        lang_meta = language_by_id[args.language]
        solution_path = problem_dir / lang_meta["file"]
        code = read_solution_file(solution_path)
        question = client.get_question(title_slug)
        leetcode_lang = repo_to_leetcode[args.language]

        if args.test_local:
            run_local_tests(repo_root, problem_dir.name, args.language)

        if args.run_only:
            data_input = question.sample_test_case.strip()
            if not data_input:
                raise LeetCodeError("No sample test case available for run-only mode.")
            interpret_id = client.run_solution(
                title_slug,
                question.question_id,
                leetcode_lang,
                code,
                data_input=data_input,
            )
            result = client.poll_submission(interpret_id, timeout=args.timeout)
        else:
            submission_id = client.submit_solution(
                title_slug,
                question.question_id,
                leetcode_lang,
                code,
            )
            print(f"Submitted: https://leetcode.com/submissions/detail/{submission_id}/")
            result = client.poll_submission(submission_id, timeout=args.timeout)

        print(format_result(result))
        status_msg = str(result.get("status_msg") or "")
        if status_msg and status_msg != "Accepted":
            return 2
        return 0
    except LeetCodeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
