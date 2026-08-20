#!/usr/bin/env python3
"""Download Go solutions from doocs/leetcode for problems 3500-3749."""
from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUBS = json.loads((ROOT / "scripts" / "_stubs_3500_3749.json").read_text(encoding="utf-8"))
REPORT = ROOT / "scripts" / "_doocs_go_report_3500_3749.json"
UA = {"User-Agent": "Mozilla/5.0", "Accept": "application/vnd.github+json"}


def is_sql(d: Path) -> bool:
    data = json.loads((d / "tests" / "cases.json").read_text(encoding="utf-8"))
    cases = data.get("cases") or []
    if any(isinstance(c, dict) and c.get("kind") == "sql" for c in cases):
        return True
    readme = (d / "README.md").read_text(encoding="utf-8", errors="replace")
    tm = re.search(r"- \*\*Tags:\*\*\s*(.+)", readme)
    return bool(tm and "database" in tm.group(1).lower())


def is_go_stub(text: str) -> bool:
    return bool(re.search(r"func solve\(\)\s*\{\s*\}", text))


def github_get(url: str) -> object:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode())


def raw_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8")


def list_range(bucket: str) -> dict[int, str]:
    """Return frontend_id -> folder name under solution/<bucket>."""
    url = f"https://api.github.com/repos/doocs/leetcode/contents/solution/{bucket}"
    entries = github_get(url)
    mapping: dict[int, str] = {}
    for e in entries:
        name = e["name"]
        m = re.match(r"^(\d+)\.", name)
        if m:
            mapping[int(m.group(1))] = name
    return mapping


def header_for(folder: str, title: str | None, slug: str | None) -> str:
    num = int(folder.split("_", 1)[0])
    nice = title or folder.split("_", 1)[1].replace("_", " ").title()
    slug = slug or folder.split("_", 1)[1].replace("_", "-")
    return (
        f"// LeetCode {num} - {nice}\n"
        f"// https://leetcode.com/problems/{slug}/\n\n"
    )


def normalize_go(code: str) -> str:
    code = code.replace("\r\n", "\n").strip() + "\n"
    # Drop package line if present (repo convention usually omits it)
    lines = code.splitlines(True)
    if lines and lines[0].startswith("package "):
        lines = lines[1:]
        while lines and lines[0].strip() == "":
            lines = lines[1:]
        code = "".join(lines)
    return code


def main() -> None:
    buckets = {
        **list_range("3500-3599"),
        **list_range("3600-3699"),
        **list_range("3700-3799"),
    }
    print(f"doocs mapped {len(buckets)} problems", flush=True)

    report = {
        "ported": [],
        "skipped_sql": [],
        "skipped_filled": [],
        "missing_doocs": [],
        "missing_go_file": [],
        "empty_go": [],
        "failures": [],
    }

    for d in sorted(ROOT.iterdir()):
        m = re.match(r"^(\d{4})_", d.name)
        if not m:
            continue
        n = int(m.group(1))
        if n < 3500 or n > 3749:
            continue
        if is_sql(d):
            report["skipped_sql"].append(d.name)
            continue
        go_path = d / "solution.go"
        existing = go_path.read_text(encoding="utf-8") if go_path.exists() else ""
        if existing and not is_go_stub(existing):
            report["skipped_filled"].append(d.name)
            continue

        doocs_name = buckets.get(n)
        if not doocs_name:
            report["missing_doocs"].append(d.name)
            continue

        bucket = f"{n // 100 * 100}-{n // 100 * 100 + 99}"
        encoded = urllib.parse.quote(doocs_name)
        raw_url = (
            f"https://raw.githubusercontent.com/doocs/leetcode/main/"
            f"solution/{bucket}/{encoded}/Solution.go"
        )
        try:
            code = raw_get(raw_url)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                report["missing_go_file"].append(d.name)
            else:
                report["failures"].append({"folder": d.name, "error": f"download: {e}"})
            continue
        except Exception as e:
            report["failures"].append({"folder": d.name, "error": f"download: {e}"})
            continue

        code = normalize_go(code)
        # Skip empty stubs from doocs
        stripped = re.sub(r"(?m)//.*$", "", code)
        if re.search(r"func \w+\([^)]*\)[^{]*\{\s*\}", stripped) and "return" not in stripped:
            report["empty_go"].append(d.name)
            continue
        if len(code.strip()) < 30:
            report["empty_go"].append(d.name)
            continue

        meta = STUBS.get(d.name, {})
        title = meta.get("title")
        slug = meta.get("slug")
        content = header_for(d.name, title, slug) + code
        go_path.write_text(content, encoding="utf-8", newline="\n")
        report["ported"].append(d.name)
        print(f"ported {d.name}", flush=True)

    out = {
        "counts": {k: len(v) for k, v in report.items()},
        "ported": report["ported"],
        "skipped_sql": report["skipped_sql"],
        "skipped_filled": report["skipped_filled"],
        "missing_doocs": report["missing_doocs"],
        "missing_go_file": report["missing_go_file"],
        "empty_go": report["empty_go"],
        "failures": report["failures"],
    }
    REPORT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("counts", out["counts"])


if __name__ == "__main__":
    main()
