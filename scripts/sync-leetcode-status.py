#!/usr/bin/env python3
"""Export your LeetCode solved-problem list to config/leetcode-solved.json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "lib"))

from leetcode_api import LeetCodeClient, LeetCodeError, folder_name  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=SCRIPT_DIR.parent.parent)
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    try:
        client = LeetCodeClient.from_env(repo_root)
        user = client.get_current_user()
        solved = client.get_solved_questions()
        entries = []
        in_repo = 0
        for item in solved:
            folder = folder_name(item.frontend_id, item.title_slug)
            has_folder = (repo_root / folder).is_dir()
            if has_folder:
                in_repo += 1
            entries.append(
                {
                    "number": item.frontend_id,
                    "title": item.title,
                    "titleSlug": item.title_slug,
                    "folder": folder,
                    "inRepo": has_folder,
                    "lastResult": item.last_result,
                }
            )

        payload = {
            "username": user.get("username"),
            "totalSolved": len(entries),
            "inRepo": in_repo,
            "entries": entries,
        }
        output_path = repo_root / "config" / "leetcode-solved.json"
        with output_path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)

        print(f"Signed in as {user.get('username')}")
        print(f"Solved on LeetCode: {len(entries)}")
        print(f"Matching repo folders: {in_repo}")
        print(f"Wrote {output_path.relative_to(repo_root)}")
        return 0
    except LeetCodeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
