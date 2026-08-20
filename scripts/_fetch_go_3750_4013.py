#!/usr/bin/env python3
"""Fetch Doocs Go solutions for problems 3750-4013 and write solution.go stubs."""
from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LO, HI = 3750, 4013
UA = {"User-Agent": "Mozilla/5.0 leetcode-sync", "Accept": "application/vnd.github+json"}


def http_get(url: str, retries: int = 3) -> bytes:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.5 * (attempt + 1))
    assert last is not None
    raise last


def list_bucket(bucket: str) -> dict[int, str]:
    url = f"https://api.github.com/repos/doocs/leetcode/contents/solution/{bucket}"
    arr = json.loads(http_get(url).decode())
    out: dict[int, str] = {}
    for item in arr:
        name = item["name"]
        m = re.match(r"^(\d+)\.", name)
        if m:
            out[int(m.group(1))] = name
    return out


def needed_imports(code: str) -> list[str]:
    pkgs: list[str] = []
    for pkg, ident in [
        ("sort", "sort."),
        ("strings", "strings."),
        ("strconv", "strconv."),
        ("math", "math."),
        ("bytes", "bytes."),
        ("regexp", "regexp."),
        ("unicode", "unicode."),
        ("container/heap", "heap."),
        ("container/list", "list."),
        ("sync", "sync."),
    ]:
        if ident in code and f'"{pkg}"' not in code:
            pkgs.append(pkg)
    return pkgs


def ensure_imports(body: str) -> str:
    if re.search(r"(?m)^import\s+", body):
        return body
    pkgs = needed_imports(body)
    if not pkgs:
        return body
    if len(pkgs) == 1:
        imp = f'import "{pkgs[0]}"\n\n'
    else:
        lines = "\n".join(f'\t"{p}"' for p in pkgs)
        imp = f"import (\n{lines}\n)\n\n"
    return imp + body.lstrip()


def strip_package(body: str) -> str:
    body = re.sub(r"(?m)^package\s+\w+\s*\n+", "", body)
    return body.strip() + "\n"


def make_header(folder: str) -> str:
    m = re.match(r"^(\d{4})_(.+)$", folder)
    assert m
    num, slug = m.group(1), m.group(2)
    title = " ".join(w.capitalize() for w in slug.split("_"))
    return (
        f"// LeetCode {num} - {title}\n"
        f"// https://leetcode.com/problems/{slug.replace('_', '-')}/\n\n"
    )


def is_sql(folder: Path) -> bool:
    cases = folder / "tests" / "cases.json"
    if not cases.exists():
        return False
    try:
        data = json.loads(cases.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    if data.get("kind") == "sql":
        return True
    for c in data.get("cases") or []:
        if isinstance(c, dict) and c.get("kind") == "sql":
            return True
    return False


def is_go_stub(text: str) -> bool:
    return bool(re.search(r"func solve\(\)\s*\{\s*\}", text))


def extract_method(code: str) -> str | None:
    methods = re.findall(r"(?m)^func\s+([A-Za-z_]\w*)\s*\(", code)
    skip = {"min", "max", "abs", "gcd", "lcm", "f", "dfs", "bfs", "solve", "main", "init"}
    for name in methods:
        if name in skip or name.startswith("_"):
            continue
        if name[0].islower() and len(name) > 2:
            return name
    for name in methods:
        if name not in skip:
            return name
    return None


def update_config(folder: Path, method: str | None) -> None:
    cfg_path = folder / "tests" / "config.json"
    if not cfg_path.exists() or not method:
        return
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    if cfg.get("method") in (None, "", "solve"):
        cfg["method"] = method
        cases_path = folder / "tests" / "cases.json"
        if cases_path.exists() and not cfg.get("paramOrder"):
            try:
                cases = json.loads(cases_path.read_text(encoding="utf-8"))
                first = (cases.get("cases") or [None])[0]
                if isinstance(first, dict) and isinstance(first.get("args"), dict):
                    cfg["paramOrder"] = list(first["args"].keys())
            except json.JSONDecodeError:
                pass
        cfg_path.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")


def fetch_solution_go(bucket: str, dirname: str) -> str | None:
    quoted = urllib.parse.quote(dirname)
    url = f"https://raw.githubusercontent.com/doocs/leetcode/main/solution/{bucket}/{quoted}/Solution.go"
    try:
        return http_get(url).decode("utf-8")
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        raise


def fetch_solution_py(bucket: str, dirname: str) -> str | None:
    quoted = urllib.parse.quote(dirname)
    url = f"https://raw.githubusercontent.com/doocs/leetcode/main/solution/{bucket}/{quoted}/Solution.py"
    try:
        return http_get(url).decode("utf-8")
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        raise


def main() -> None:
    buckets = {
        "3700-3799": list_bucket("3700-3799"),
        "3800-3899": list_bucket("3800-3899"),
        "3900-3999": list_bucket("3900-3999"),
        "4000-4099": list_bucket("4000-4099"),
    }
    num_to_loc: dict[int, tuple[str, str]] = {}
    for bucket, mapping in buckets.items():
        for num, name in mapping.items():
            num_to_loc[num] = (bucket, name)

    ported: list[str] = []
    skipped_sql: list[str] = []
    skipped_filled: list[str] = []
    missing_go: list[str] = []
    failures: list[str] = []
    py_saved: list[str] = []

    for d in sorted(ROOT.iterdir()):
        if not d.is_dir():
            continue
        m = re.match(r"^(\d{4})_(.+)$", d.name)
        if not m:
            continue
        n = int(m.group(1))
        if n < LO or n > HI:
            continue
        go_path = d / "solution.go"
        if not go_path.exists():
            failures.append(f"{d.name}: no solution.go")
            continue
        existing = go_path.read_text(encoding="utf-8", errors="replace")
        if not is_go_stub(existing):
            skipped_filled.append(d.name)
            continue
        if is_sql(d):
            skipped_sql.append(d.name)
            continue

        loc = num_to_loc.get(n)
        if not loc:
            failures.append(f"{d.name}: not on doocs")
            continue
        bucket, dirname = loc
        code = fetch_solution_go(bucket, dirname)
        if code is None:
            py = fetch_solution_py(bucket, dirname)
            if py:
                py_path = d / "solution.py"
                cur = py_path.read_text(encoding="utf-8", errors="replace") if py_path.exists() else ""
                if "def solve(self)" in cur and cur.strip().endswith("pass"):
                    header = f"# LeetCode {m.group(1)} - {' '.join(w.capitalize() for w in m.group(2).split('_'))}\n"
                    header += f"# https://leetcode.com/problems/{m.group(2).replace('_', '-')}/\n\n"
                    py_path.write_text(header + py.lstrip(), encoding="utf-8", newline="\n")
                    py_saved.append(d.name)
            missing_go.append(d.name)
            continue

        body = ensure_imports(strip_package(code))
        content = make_header(d.name) + body
        go_path.write_text(content, encoding="utf-8", newline="\n")
        method = extract_method(body)
        update_config(d, method)
        ported.append(d.name)
        time.sleep(0.05)

    report = {
        "ported": len(ported),
        "skipped_sql": skipped_sql,
        "skipped_filled": skipped_filled,
        "missing_go": missing_go,
        "py_saved_for_missing_go": py_saved,
        "failures": failures,
        "ported_folders": ported,
    }
    out = ROOT / "scripts" / "_fetch_go_3750_4013_report.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in report.items()}, indent=2))
    print("wrote", out)
    if missing_go:
        print("MISSING_GO:")
        for name in missing_go:
            print(" ", name)


if __name__ == "__main__":
    main()
