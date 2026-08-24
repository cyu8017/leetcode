#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
batch = (ROOT / ".tmp_php4013/batch_21.txt").read_text().strip().splitlines()

SOLUTIONS = {}
for name in ["port_batch21_a", "port_batch21_b", "port_batch21_c", "port_batch21_d"]:
    ns = {}
    exec((ROOT / f".tmp_php4013/{name}.py").read_text(), ns)
    SOLUTIONS.update(ns["SOLUTIONS"])

written = 0
missing = []
for folder in batch:
    if folder not in SOLUTIONS:
        missing.append(folder)
        continue
    body = SOLUTIONS[folder]
    if not body.endswith("\n"):
        body += "\n"
    path = ROOT / folder / "solution.php"
    path.write_text(body, encoding="utf-8", newline="\n")
    written += 1

print(f"written={written}")
print(f"defined={len(SOLUTIONS)}")
if missing:
    print("MISSING:")
    for m in missing:
        print(m)
