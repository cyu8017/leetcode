from pathlib import Path
import json
import re

left = [ln for ln in Path("scripts/_go_stubs_left_3500.txt").read_text().splitlines() if ln]
text = Path("scripts/_port_go_remaining_b5.py").read_text(encoding="utf-8")
keys = re.findall(r'S\["([^"]+)"\]', text)
print("left", len(left))
print("keys", len(keys))
missing = [x for x in left if x not in keys]
print("missing from S:")
for x in missing:
    print(x)
st = json.loads(Path("scripts/_stubs_3500_3749.json").read_text(encoding="utf-8"))
print("3529", st.get("3529_count_cells_in_overlapping_horizontal_and_vertical_substrings", {}).get("go", "")[:300])
