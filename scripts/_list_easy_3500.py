#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def is_sql(d: Path) -> bool:
    data = json.loads((d / "tests" / "cases.json").read_text(encoding="utf-8"))
    cases = data.get("cases") or []
    if any(isinstance(c, dict) and c.get("kind") == "sql" for c in cases):
        return True
    readme = (d / "README.md").read_text(encoding="utf-8", errors="replace")
    tm = re.search(r"- \*\*Tags:\*\*\s*(.+)", readme)
    if tm and "database" in tm.group(1).lower():
        return True
    return False


def main() -> None:
    easy = []
    for d in sorted(ROOT.iterdir()):
        m = re.match(r"^(\d{4})_", d.name)
        if not m:
            continue
        n = int(m.group(1))
        if n < 3500 or n > 3749:
            continue
        if is_sql(d):
            continue
        readme = (d / "README.md").read_text(encoding="utf-8", errors="replace")
        dm = re.search(r"\*\*Difficulty:\*\*\s*(\w+)", readme)
        if not dm or dm.group(1) != "Easy":
            continue
        cfg = json.loads((d / "tests" / "config.json").read_text(encoding="utf-8"))
        easy.append(
            {
                "folder": d.name,
                "method": cfg.get("method"),
                "class": cfg.get("class"),
                "params": cfg.get("paramOrder"),
                "kind": cfg.get("kind"),
            }
        )
    out = ROOT / "scripts" / "_easy_3500_3749.json"
    out.write_text(json.dumps(easy, indent=2), encoding="utf-8")
    print(len(easy))
    for e in easy:
        print(e["folder"], e["method"], e["params"])


if __name__ == "__main__":
    main()
