import os
from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
batches = []
for f in ["batch_21.txt", "batch_22.txt"]:
    p = root / ".tmp_sw4013" / f
    batches.extend([line.strip() for line in p.read_text().splitlines() if line.strip()])

print(f"Total folders: {len(batches)}")


def is_swift_stub(text):
    if "func solve()" in text:
        return True
    lines = [l.strip() for l in text.splitlines() if l.strip() and not l.strip().startswith("//")]
    body = "\n".join(lines)
    if "TODO" in body and len(lines) < 15:
        return True
    if "fatalError" in body and len(lines) < 15:
        return True
    return False


stubs = []
implemented = []
missing = []
for folder in batches:
    sw = root / folder / "Solution.swift"
    if not sw.exists():
        missing.append(folder)
        continue
    text = sw.read_text()
    if is_swift_stub(text):
        stubs.append(folder)
    else:
        implemented.append(folder)

print(f"Stubs: {len(stubs)}")
print(f"Implemented: {len(implemented)}")
print(f"Missing: {len(missing)}")
if implemented:
    print("IMPLEMENTED:")
    for x in implemented:
        print(" ", x)
if missing:
    print("MISSING:")
    for x in missing:
        print(" ", x)

langs = [
    ("Solution.java", "java"),
    ("solution.cpp", "cpp"),
    ("Solution.kt", "kt"),
    ("solution.py", "py"),
    ("solution.js", "js"),
    ("solution.ts", "ts"),
    ("solution.go", "go"),
]


def src_stub(text):
    t = text.strip()
    if "func solve()" in t or "def solve(" in t:
        return True
    if "TODO" in t and len(t.splitlines()) < 15:
        return True
    if "NotImplemented" in t:
        return True
    if "throw new UnsupportedOperationException" in t:
        return True
    if "unimplemented!" in t:
        return True
    # very short empty bodies
    if len(t.splitlines()) <= 8 and ("pass" in t or "{}" in t):
        return True
    return False


print("\n=== SOURCE STATUS FOR STUBS ===")
src_counts = {k: 0 for _, k in langs}
no_src = []
src_map = {}
for folder in stubs:
    found = []
    for fname, lang in langs:
        p = root / folder / fname
        if p.exists():
            text = p.read_text()
            if not src_stub(text):
                found.append(lang)
                src_counts[lang] += 1
    src_map[folder] = found
    if not found:
        no_src.append(folder)

print("Source counts (non-stub):", src_counts)
print(f"No usable source: {len(no_src)}")
for x in no_src:
    print("  NOSRC", x)

# method names from python
print("\n=== SAMPLE PYTHON METHOD NAMES ===")
for folder in stubs[:15]:
    py = root / folder / "solution.py"
    if py.exists():
        for line in py.read_text().splitlines():
            if line.strip().startswith("def ") and "solve" not in line:
                print(folder, line.strip()[:80])
                break
        else:
            print(folder, "NO DEF")
    else:
        print(folder, "NO PY")
