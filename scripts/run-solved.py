#!/usr/bin/env python3
"""Run tests for all problems listed in config/solved-problems.json."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "lib"))

from test_runner import run_docker, run_local  # noqa: E402


DEFAULT_LANGUAGES = [
    "python",
    "javascript",
    "typescript",
    "java",
    "ruby",
    "php",
    "cpp",
    "c",
    "go",
    "rust",
    "csharp",
    "kotlin",
    "scala",
    "swift",
]


def load_manifest(repo_root: Path) -> list[dict]:
    manifest_path = repo_root / "config" / "solved-problems.json"
    payload = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    return payload.get("entries", [])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--language", action="append", dest="languages", help="Filter to language(s)")
    parser.add_argument("--local", action="store_true", help="Use host toolchains instead of Docker")
    parser.add_argument("--fail-fast", action="store_true", help="Stop on first failure")
    parser.add_argument("--folder", help="Run a single manifest folder only")
    args = parser.parse_args()

    repo_root = args.repo_root
    entries = load_manifest(repo_root)
    if args.folder:
        entries = [entry for entry in entries if entry["folder"] == args.folder]
        if not entries:
            print(f"Folder not in solved manifest: {args.folder}", file=sys.stderr)
            return 2

    if not args.local and not shutil.which("docker"):
        print("Docker is required unless --local is passed.", file=sys.stderr)
        return 2

    runner = run_local if args.local else run_docker
    results: list[tuple[str, str, int]] = []

    for entry in entries:
        folder = entry["folder"]
        languages = args.languages or entry.get("languages") or ["python"]
        for language in languages:
            exit_code = runner(repo_root, folder, language.lower())
            results.append((folder, language.lower(), exit_code))
            if exit_code != 0 and args.fail_fast:
                break
        if args.fail_fast and results and results[-1][2] != 0:
            break

    passed = sum(1 for _, _, code in results if code == 0)
    failed = [(folder, language, code) for folder, language, code in results if code != 0]

    print("\nSummary")
    print(f"  Passed: {passed}/{len(results)}")
    for folder, language, code in failed:
        print(f"  FAIL {folder} [{language}] exit={code}")

    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
