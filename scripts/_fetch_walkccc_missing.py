#!/usr/bin/env python3
"""Fetch walkccc Python sources for remaining 3500-3749 Go gaps."""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = json.loads((ROOT / "scripts" / "_doocs_go_report_3500_3749.json").read_text(encoding="utf-8"))
OUT = ROOT / "scripts" / "_walkccc_py_3500_3749.json"
TREE_CACHE = ROOT / "scripts" / "_walkccc_tree.json"
UA = {"User-Agent": "Mozilla/5.0", "Accept": "application/vnd.github+json"}


def load_tree() -> list[str]:
    if TREE_CACHE.exists():
        return json.loads(TREE_CACHE.read_text(encoding="utf-8"))
    url = "https://api.github.com/repos/walkccc/LeetCode/git/trees/main?recursive=1"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode())
    paths = [t["path"] for t in data.get("tree", [])]
    TREE_CACHE.write_text(json.dumps(paths), encoding="utf-8")
    return paths


def main() -> None:
    paths = load_tree()
    by_num: dict[int, dict[str, str]] = {}
    for p in paths:
        m = re.match(r"^solutions/(\d+)\.[^/]+/(\d+)\.(py|cpp|java)$", p)
        if not m:
            continue
        n = int(m.group(1))
        if n < 3500 or n > 3749:
            continue
        by_num.setdefault(n, {})[m.group(3)] = p

    missing = REPORT["missing_go_file"]
    results = {}
    for folder in missing:
        n = int(folder.split("_", 1)[0])
        langs = by_num.get(n, {})
        entry = {"langs": list(langs), "py": None, "cpp": None}
        for lang in ("py", "cpp"):
            if lang not in langs:
                continue
            raw = (
                "https://raw.githubusercontent.com/walkccc/LeetCode/main/"
                + urllib.parse.quote(langs[lang])
            )
            try:
                req = urllib.request.Request(raw, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=30) as resp:
                    entry[lang] = resp.read().decode("utf-8")
            except Exception as e:
                entry[f"{lang}_error"] = str(e)
        results[folder] = entry
        print(folder, "langs", entry["langs"], "py", bool(entry["py"]), flush=True)

    OUT.write_text(json.dumps(results, indent=2), encoding="utf-8")
    have_py = sum(1 for v in results.values() if v.get("py"))
    have_cpp = sum(1 for v in results.values() if v.get("cpp"))
    none = sum(1 for v in results.values() if not v.get("py") and not v.get("cpp"))
    print(f"have_py={have_py} have_cpp={have_cpp} none={none} total={len(results)}")


if __name__ == "__main__":
    main()
