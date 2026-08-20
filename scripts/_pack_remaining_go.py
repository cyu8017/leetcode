#!/usr/bin/env python3
"""Dump stubs + walkccc sources for remaining gaps into a working set."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
stubs = json.loads((ROOT / "scripts" / "_stubs_3500_3749.json").read_text(encoding="utf-8"))
report = json.loads((ROOT / "scripts" / "_doocs_go_report_3500_3749.json").read_text(encoding="utf-8"))
walk = json.loads((ROOT / "scripts" / "_walkccc_py_3500_3749.json").read_text(encoding="utf-8"))

out = {}
for folder in report["missing_go_file"]:
    out[folder] = {
        "go_stub": stubs.get(folder, {}).get("go"),
        "py_stub": stubs.get(folder, {}).get("py"),
        "walk_py": walk.get(folder, {}).get("py"),
        "walk_cpp": walk.get(folder, {}).get("cpp"),
        "paid": stubs.get(folder, {}).get("paid"),
        "title": stubs.get(folder, {}).get("title"),
        "slug": stubs.get(folder, {}).get("slug"),
    }

path = ROOT / "scripts" / "_remaining_go_3500_3749.json"
path.write_text(json.dumps(out, indent=2), encoding="utf-8")
print("remaining", len(out))
print("with walk py", sum(1 for v in out.values() if v["walk_py"]))
print("with walk cpp only", sum(1 for v in out.values() if not v["walk_py"] and v["walk_cpp"]))
print("with go stub", sum(1 for v in out.values() if v["go_stub"]))
print("no stub no walk", sum(1 for v in out.values() if not v["go_stub"] and not v["walk_py"] and not v["walk_cpp"]))
