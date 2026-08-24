import re
from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
batches = []
for f in ["batch_21.txt", "batch_22.txt"]:
    p = root / ".tmp_sw4013" / f
    batches.extend([line.strip() for line in p.read_text().splitlines() if line.strip()])

out = []
for folder in batches:
    java = (root / folder / "Solution.java").read_text()
    lines = java.splitlines()
    nlines = len(lines)
    methods = re.findall(r"public\s+[\w<>,\s\[\]]+\s+(\w+)\s*\([^;]*\)\s*\{", java)
    classes = re.findall(r"(?:class|interface)\s+(\w+)", java)
    has_listnode = "ListNode" in java
    has_treenode = "TreeNode" in java
    has_node = re.search(r"\bclass Node\b", java) is not None
    has_design = "class Solution" not in java or (len(classes) > 1 and "Solution" not in classes[:1])
    # design if no Solution class
    is_design = "class Solution" not in java
    out.append((folder, nlines, methods, classes, has_listnode, has_treenode, is_design))

# sort by lines
out_sorted = sorted(out, key=lambda x: -x[1])
print("LONGEST:")
for row in out_sorted[:30]:
    print(f"  {row[1]:4d} {row[0]} methods={row[2]} classes={row[3]} list={row[4]} tree={row[5]} design={row[6]}")

print("\nDESIGN:")
for row in out:
    if row[6] or (row[3] and "Solution" not in row[3]):
        print(f"  {row[0]} classes={row[3]} methods={row[2]}")

print("\nTREE/LIST:")
for row in out:
    if row[4] or row[5]:
        print(f"  {row[0]} list={row[4]} tree={row[5]}")

print("\nLINE DISTRIBUTION:")
buckets = [0, 0, 0, 0, 0]
for row in out:
    n = row[1]
    if n < 20:
        buckets[0] += 1
    elif n < 40:
        buckets[1] += 1
    elif n < 80:
        buckets[2] += 1
    elif n < 150:
        buckets[3] += 1
    else:
        buckets[4] += 1
print("  <20", buckets[0], "<40", buckets[1], "<80", buckets[2], "<150", buckets[3], ">=150", buckets[4])

# dump all signatures
print("\n=== ALL SIGNATURES ===")
for row in out:
    print(f"{row[0]}|{row[1]}|{','.join(row[2])}|{','.join(row[3])}")
