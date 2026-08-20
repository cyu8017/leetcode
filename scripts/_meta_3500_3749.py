#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = []
sql = []
for d in sorted(ROOT.iterdir()):
    if not d.is_dir():
        continue
    m = re.match(r"^(\d{4})_(.+)$", d.name)
    if not m:
        continue
    n = int(m.group(1))
    if n < 3500 or n > 3749:
        continue
    cases = d / "tests" / "cases.json"
    kind = None
    if cases.exists():
        try:
            data = json.loads(cases.read_text(encoding="utf-8"))
            kind = data.get("kind")
        except Exception as e:
            kind = f"err:{e}"
    if kind == "sql":
        sql.append(d.name)
        continue
    cfg = json.loads((d / "tests" / "config.json").read_text(encoding="utf-8"))
    readme = (d / "README.md").read_text(encoding="utf-8", errors="replace")
    diff = "Unknown"
    dm = re.search(r"\*\*Difficulty:\*\*\s*(\w+)", readme)
    if dm:
        diff = dm.group(1)
    go = (d / "solution.go").read_text(encoding="utf-8")
    is_stub = bool(re.search(r"func solve\(\)\s*\{\s*\}", go))
    rows.append(
        {
            "folder": d.name,
            "num": n,
            "method": cfg.get("method"),
            "class": cfg.get("class"),
            "params": cfg.get("paramOrder"),
            "kind": kind,
            "diff": diff,
            "stub": is_stub,
        }
    )

out = ROOT / "scripts" / "_meta_3500_3749.json"
out.write_text(json.dumps({"sql": sql, "rows": rows}, indent=2), encoding="utf-8")
print("non_sql", len(rows), "sql", len(sql), "stubs", sum(1 for r in rows if r["stub"]))
print("wrote", out)
