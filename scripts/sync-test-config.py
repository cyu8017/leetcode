#!/usr/bin/env python3
"""Refresh tests/config.json from cases + LeetCode metadata without touching cases.json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "lib"))

from test_config import build_config, metadata_from_neenza  # noqa: E402


def load_json(path: Path, default=None):
    if not path.exists():
        return default
    with path.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def save_json(path: Path, payload) -> None:
    temp_path = path.with_suffix(path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    temp_path.replace(path)


def folder_name(number: int, title_slug: str) -> str:
    return f"{number:04d}_{title_slug.replace('-', '_')}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=SCRIPT_DIR.parent)
    parser.add_argument("--number", type=int, help="Sync one problem number")
    parser.add_argument("--force", action="store_true", help="Update even when method is already set")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    neenza_raw = load_json(repo_root / "config" / "neenza-problems.json", default={}) or {}
    neenza_by_id = {
        item["frontend_id"]: item for item in neenza_raw.get("questions", []) if item.get("frontend_id")
    }

    targets = sorted(repo_root.glob("*/tests/cases.json"))
    if args.number is not None:
        targets = [path for path in targets if path.parent.parent.name.startswith(f"{args.number:04d}_")]

    updated = 0
    skipped = 0

    for cases_path in targets:
        problem_dir = cases_path.parent.parent
        folder = problem_dir.name
        config_path = cases_path.parent / "config.json"

        cases_doc = load_json(cases_path, default={"cases": []}) or {"cases": []}
        cases = cases_doc.get("cases") or []
        if not cases:
            skipped += 1
            continue

        existing = load_json(config_path, default={}) or {}
        if existing.get("method") and existing.get("method") != "solve" and not args.force:
            if existing.get("kind") in {"design", "sql", "shell"}:
                skipped += 1
                continue

        try:
            number = int(folder.split("_", 1)[0])
        except ValueError:
            skipped += 1
            continue

        metadata = metadata_from_neenza(neenza_by_id.get(str(number)))
        config = build_config(existing, metadata, cases)

        if config == existing:
            skipped += 1
            continue

        if args.dry_run:
            print(f"DRY {folder}: method={config.get('method')} kind={config.get('kind', 'standard')}")
            updated += 1
            continue

        save_json(config_path, config)
        updated += 1
        if updated % 500 == 0:
            print(f"Updated {updated} configs...")

    print(f"Done. updated={updated}, skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
