#!/usr/bin/env python3
"""Fetch Go + Python3 code stubs from LeetCode for 3500-3749."""
from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "scripts" / "_stubs_3500_3749.json"
QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    isPaidOnly
    codeSnippets { langSlug code }
  }
}
"""


def is_sql(d: Path) -> bool:
    data = json.loads((d / "tests" / "cases.json").read_text(encoding="utf-8"))
    cases = data.get("cases") or []
    if any(isinstance(c, dict) and c.get("kind") == "sql" for c in cases):
        return True
    readme = (d / "README.md").read_text(encoding="utf-8", errors="replace")
    tm = re.search(r"- \*\*Tags:\*\*\s*(.+)", readme)
    return bool(tm and "database" in tm.group(1).lower())


def slug_from_folder(name: str) -> str:
    # 3516_find_closest_person -> find-closest-person
    m = re.match(r"^\d{4}_(.+)$", name)
    assert m
    return m.group(1).replace("_", "-")


def fetch(slug: str) -> dict:
    body = json.dumps({"query": QUERY, "variables": {"titleSlug": slug}}).encode()
    req = urllib.request.Request(
        "https://leetcode.com/graphql",
        data=body,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Referer": f"https://leetcode.com/problems/{slug}/",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode())
    if data.get("errors"):
        raise RuntimeError(str(data["errors"]))
    return data["data"]["question"]


def main() -> None:
    results = {}
    if OUT.exists():
        results = json.loads(OUT.read_text(encoding="utf-8"))

    folders = []
    for d in sorted(ROOT.iterdir()):
        m = re.match(r"^(\d{4})_", d.name)
        if not m:
            continue
        n = int(m.group(1))
        if n < 3500 or n > 3749:
            continue
        if is_sql(d):
            results[d.name] = {"skip": "sql"}
            continue
        folders.append(d.name)

    for i, folder in enumerate(folders):
        if folder in results and results[folder].get("go"):
            continue
        slug = slug_from_folder(folder)
        print(f"[{i+1}/{len(folders)}] {folder}", flush=True)
        try:
            q = fetch(slug)
            go = next((s["code"] for s in (q.get("codeSnippets") or []) if s["langSlug"] == "golang"), None)
            py = next((s["code"] for s in (q.get("codeSnippets") or []) if s["langSlug"] == "python3"), None)
            results[folder] = {
                "slug": slug,
                "title": q.get("title"),
                "paid": q.get("isPaidOnly"),
                "go": go,
                "py": py,
            }
        except Exception as e:
            results[folder] = {"slug": slug, "error": str(e)}
            print("  ERR", e)
        OUT.write_text(json.dumps(results, indent=2), encoding="utf-8")
        time.sleep(0.25)

    have_go = sum(1 for v in results.values() if v.get("go"))
    sql = sum(1 for v in results.values() if v.get("skip") == "sql")
    err = sum(1 for v in results.values() if v.get("error"))
    print(f"done have_go={have_go} sql={sql} err={err} total={len(results)}")


if __name__ == "__main__":
    main()
