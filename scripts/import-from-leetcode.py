#!/usr/bin/env python3
"""Import accepted LeetCode submissions into local solution files."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "lib"))

from leetcode_api import (  # noqa: E402
    LeetCodeClient,
    LeetCodeError,
    SubmissionOverview,
    find_folder,
    folder_name,
    load_language_maps,
    parse_folder_name,
    write_solution_file,
)


def build_targets(
    client: LeetCodeClient,
    repo_root: Path,
    *,
    folder: str | None,
    number: int | None,
    import_all: bool,
    limit: int | None,
) -> list[tuple[int, str, str, str]]:
    if folder or number is not None:
        problem_dir = find_folder(repo_root, number=number, folder=folder)
        num, slug = parse_folder_name(problem_dir.name)
        question = client.get_question(slug)
        return [(num, question.title, slug, problem_dir.name)]

    solved = client.get_solved_questions()
    if limit is not None:
        solved = solved[:limit]

    targets: list[tuple[int, str, str, str]] = []
    for item in solved:
        name = folder_name(item.frontend_id, item.title_slug)
        if not (repo_root / name).is_dir():
            continue
        targets.append((item.frontend_id, item.title, item.title_slug, name))
    return targets


def import_one(
    client: LeetCodeClient,
    repo_root: Path,
    *,
    number: int,
    title: str,
    title_slug: str,
    folder: str,
    language_by_id: dict[str, dict[str, str]],
    leetcode_to_repo: dict[str, str],
    preferred_language: str | None,
    all_languages: bool,
    overwrite: bool,
    dry_run: bool,
) -> list[dict[str, str]]:
    if all_languages:
        submissions = client.get_accepted_submissions_by_language(title_slug)
        if not submissions:
            return [{"status": "skipped", "reason": "no accepted submissions", "folder": folder}]

        outcomes: list[dict[str, str]] = []
        for lang_key, overview in submissions.items():
            repo_lang = leetcode_to_repo.get(lang_key)
            if repo_lang is None:
                outcomes.append(
                    {
                        "status": "skipped",
                        "reason": f"unsupported LeetCode language '{lang_key}'",
                        "folder": folder,
                    }
                )
                continue
            if preferred_language and repo_lang != preferred_language:
                continue
            outcomes.append(
                _import_submission(
                    client,
                    repo_root,
                    number=number,
                    title=title,
                    title_slug=title_slug,
                    folder=folder,
                    repo_lang=repo_lang,
                    language_by_id=language_by_id,
                    overview=overview,
                    overwrite=overwrite,
                    dry_run=dry_run,
                )
            )
        if not outcomes:
            return [{"status": "skipped", "reason": "no matching languages", "folder": folder}]
        return outcomes

    overview = client.get_latest_accepted_submission(title_slug)
    if overview is None:
        return [{"status": "skipped", "reason": "no accepted submission", "folder": folder}]

    repo_lang = leetcode_to_repo.get(overview.lang_slug)
    if repo_lang is None:
        return [
            {
                "status": "skipped",
                "reason": f"unsupported LeetCode language '{overview.lang_slug}'",
                "folder": folder,
            }
        ]
    if preferred_language and repo_lang != preferred_language:
        return [{"status": "skipped", "reason": f"language is {repo_lang}, not {preferred_language}", "folder": folder}]

    return [
        _import_submission(
            client,
            repo_root,
            number=number,
            title=title,
            title_slug=title_slug,
            folder=folder,
            repo_lang=repo_lang,
            language_by_id=language_by_id,
            overview=overview,
            overwrite=overwrite,
            dry_run=dry_run,
        )
    ]


def _import_submission(
    client: LeetCodeClient,
    repo_root: Path,
    *,
    number: int,
    title: str,
    title_slug: str,
    folder: str,
    repo_lang: str,
    language_by_id: dict[str, dict[str, str]],
    overview: SubmissionOverview,
    overwrite: bool,
    dry_run: bool,
) -> dict[str, str]:
    lang_meta = language_by_id[repo_lang]
    solution_path = repo_root / folder / lang_meta["file"]
    if solution_path.exists() and not overwrite:
        return {
            "status": "skipped",
            "reason": "file exists (use --overwrite)",
            "folder": folder,
            "language": repo_lang,
        }

    code = client.get_submission_code(overview.submission_id)
    if dry_run:
        return {
            "status": "dry-run",
            "language": repo_lang,
            "file": str(solution_path.relative_to(repo_root)),
            "bytes": str(len(code.encode("utf-8"))),
            "folder": folder,
        }

    write_solution_file(
        solution_path,
        code,
        number=number,
        title=title,
        title_slug=title_slug,
        comment=lang_meta["comment"],
    )
    return {
        "status": "imported",
        "language": repo_lang,
        "file": str(solution_path.relative_to(repo_root)),
        "folder": folder,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=SCRIPT_DIR.parent.parent)
    parser.add_argument("--folder", help="Problem folder, e.g. 0001_two_sum")
    parser.add_argument("--number", type=int, help="Problem number, e.g. 1")
    parser.add_argument("--all", action="store_true", help="Import all solved problems")
    parser.add_argument(
        "--all-languages",
        action="store_true",
        help="Import latest accepted submission per language (not just the most recent one)",
    )
    parser.add_argument("--language", help="Only import if submission language matches repo language id")
    parser.add_argument("--limit", type=int, help="Max problems when using --all")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing solution files")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    if not args.all and not args.folder and args.number is None:
        parser.error("Provide --folder, --number, or --all")

    try:
        client = LeetCodeClient.from_env(repo_root)
        user = client.get_current_user()
        print(f"Signed in as {user.get('username')}")

        language_by_id, leetcode_to_repo, _ = load_language_maps(repo_root)
        if args.language and args.language not in language_by_id:
            raise LeetCodeError(f"Unknown language id: {args.language}")

        targets = build_targets(
            client,
            repo_root,
            folder=args.folder,
            number=args.number,
            import_all=args.all,
            limit=args.limit,
        )
        if not targets:
            print("No matching problems to import.")
            return 0

        results: list[dict[str, str]] = []
        for number, title, title_slug, folder in targets:
            outcomes = import_one(
                client,
                repo_root,
                number=number,
                title=title,
                title_slug=title_slug,
                folder=folder,
                language_by_id=language_by_id,
                leetcode_to_repo=leetcode_to_repo,
                preferred_language=args.language,
                all_languages=args.all_languages,
                overwrite=args.overwrite,
                dry_run=args.dry_run,
            )
            for outcome in outcomes:
                results.append(outcome)
                status = outcome["status"]
                language = outcome.get("language", "")
                detail = outcome.get("reason") or outcome.get("file") or ""
                suffix = f" [{language}]" if language else ""
                print(f"{folder}{suffix}: {status} {detail}".rstrip())

        summary = {
            "username": user.get("username"),
            "imported": sum(1 for item in results if item["status"] == "imported"),
            "skipped": sum(1 for item in results if item["status"] == "skipped"),
            "dry_run": sum(1 for item in results if item["status"] == "dry-run"),
            "results": results,
        }
        report_path = repo_root / "config" / "last-leetcode-import.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with report_path.open("w", encoding="utf-8") as handle:
            json.dump(summary, handle, indent=2)
        print(f"\nReport: {report_path.relative_to(repo_root)}")
        return 0
    except LeetCodeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
