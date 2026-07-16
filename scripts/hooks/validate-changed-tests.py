#!/usr/bin/env python3
"""Validate test JSON for folders touched in the current commit."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def changed_test_folders(repo_root: Path) -> set[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    folders: set[str] = set()
    for line in result.stdout.splitlines():
        parts = line.strip().split("/")
        if len(parts) >= 3 and parts[1] == "tests":
            folders.add(parts[0])
    return folders


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    folders = changed_test_folders(repo_root)
    if not folders:
        return 0

    validate_script = repo_root / "scripts" / "validate-repo.py"
    exit_code = 0
    for folder in sorted(folders):
        completed = subprocess.run(
            [sys.executable, str(validate_script), "--repo-root", str(repo_root), "--folder", folder],
            cwd=repo_root,
        )
        if completed.returncode != 0:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
