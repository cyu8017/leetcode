#!/usr/bin/env python3
"""Run tests for a problem and add it to config/solved-problems.json."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "lib"))

from test_runner import run_docker, run_local  # noqa: E402


def load_manifest(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8-sig"))
    return {"description": "Problems with passing implementations.", "entries": []}


def save_manifest(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def upsert_entry(entries: list[dict], folder: str, language: str) -> list[dict]:
    language = language.lower()
    for entry in entries:
        if entry["folder"] != folder:
            continue
        languages = [lang.lower() for lang in entry.get("languages") or []]
        if language not in languages:
            languages.append(language)
        entry["languages"] = sorted(set(languages))
        return entries

    entries.append({"folder": folder, "languages": [language]})
    entries.sort(key=lambda item: item["folder"])
    return entries


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=SCRIPT_DIR.parent)
    parser.add_argument("--folder", required=True)
    parser.add_argument("--language", required=True)
    parser.add_argument("--local", action="store_true")
    parser.add_argument("--skip-test", action="store_true")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    problem_dir = repo_root / args.folder
    if not problem_dir.is_dir():
        print(f"Missing folder: {args.folder}", file=sys.stderr)
        return 2

    if not args.skip_test:
        runner = run_local if args.local else run_docker
        exit_code = runner(repo_root, args.folder, args.language.lower())
        if exit_code != 0:
            print("Tests failed; not updating solved manifest.", file=sys.stderr)
            return exit_code

    manifest_path = repo_root / "config" / "solved-problems.json"
    payload = load_manifest(manifest_path)
    payload["entries"] = upsert_entry(payload.get("entries") or [], args.folder, args.language)
    save_manifest(manifest_path, payload)
    print(f"Updated {manifest_path.relative_to(repo_root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
