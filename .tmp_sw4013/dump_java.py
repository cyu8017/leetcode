from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
batches = []
for f in ["batch_21.txt", "batch_22.txt"]:
    p = root / ".tmp_sw4013" / f
    batches.extend([line.strip() for line in p.read_text().splitlines() if line.strip()])

out_dir = root / ".tmp_sw4013" / "java_dump"
out_dir.mkdir(exist_ok=True)

chunk = 20
for i in range(0, len(batches), chunk):
    part = batches[i : i + chunk]
    lines = []
    for folder in part:
        java = (root / folder / "Solution.java").read_text()
        n = len(java.splitlines())
        lines.append("=" * 80)
        lines.append(f"{folder}  lines={n}")
        lines.append("=" * 80)
        lines.append(java)
        lines.append("")
    (out_dir / f"chunk_{i//chunk:02d}.txt").write_text("\n".join(lines))
print("wrote", (len(batches) + chunk - 1) // chunk, "chunks")
