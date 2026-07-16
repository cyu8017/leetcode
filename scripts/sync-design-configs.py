#!/usr/bin/env python3
"""Set tests/config.json from cases + metadata (design, sql, shell, standard)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "lib"))

from test_config import build_config  # noqa: E402


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    updated = 0

    for cases_path in sorted(repo_root.glob("*/tests/cases.json")):
        config_path = cases_path.parent / "config.json"
        cases_doc = json.loads(cases_path.read_text(encoding="utf-8-sig"))
        cases = cases_doc.get("cases") or []
        if not cases:
            continue

        existing = json.loads(config_path.read_text(encoding="utf-8-sig")) if config_path.exists() else {}
        config = build_config(existing, None, cases)
        if config == existing:
            continue

        with config_path.open("w", encoding="utf-8") as handle:
            json.dump(config, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
        updated += 1

    print(f"Updated {updated} problem configs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
