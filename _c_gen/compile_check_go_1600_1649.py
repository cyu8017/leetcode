#!/usr/bin/env python3
"""Compile-check Go solutions for 1600-1649 (non-SQL)."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SQL = {1607, 1613, 1623, 1633, 1635, 1645}


def with_package(src: str) -> str:
    if re.search(r"(?m)^package ", src):
        return src
    lines = src.splitlines(True)
    i = 0
    while i < len(lines) and (lines[i].startswith("//") or lines[i].strip() == ""):
        i += 1
    lines.insert(i, "package main\n\n")
    return "".join(lines)


def main() -> int:
    ok: list[str] = []
    fail: list[tuple[str, str]] = []
    for n in range(1600, 1650):
        if n in SQL:
            continue
        folders = list(ROOT.glob(f"{n:04d}_*"))
        if not folders:
            fail.append((f"{n}", "missing folder"))
            continue
        folder = folders[0]
        path = folder / "solution.go"
        src = path.read_text(encoding="utf-8")
        if re.search(r"func solve\s*\(", src):
            fail.append((folder.name, "still stub"))
            continue
        body = with_package(src)
        with tempfile.TemporaryDirectory() as td:
            out_go = Path(td) / "solution.go"
            out_bin = Path(td) / "out"
            out_go.write_text(body, encoding="utf-8")
            r = subprocess.run(
                ["go", "build", "-o", str(out_bin), str(out_go)],
                capture_output=True,
                text=True,
            )
            if r.returncode == 0:
                ok.append(folder.name)
            else:
                err = (r.stderr or r.stdout or "").strip()
                fail.append((folder.name, err))

    print(f"OK {len(ok)} FAIL {len(fail)}")
    for name, err in fail:
        print(f"FAIL {name}")
        print(err[:1000])
        print("---")
    return 0 if not fail else 1


if __name__ == "__main__":
    raise SystemExit(main())
