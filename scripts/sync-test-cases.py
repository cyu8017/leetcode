#!/usr/bin/env python3
"""Sync LeetCode example test cases into each problem's tests/cases.json."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "lib"))

from example_parser import (  # noqa: E402
    parse_example_text,
    parse_examples_from_html,
    parse_examples_from_markdown,
)
from test_config import build_config, metadata_from_neenza  # noqa: E402

NEENZA_URL = "https://raw.githubusercontent.com/neenza/leetcode-problems/master/merged_problems.json"
DEFAULT_QUESTIONS_URL = (
    "https://raw.githubusercontent.com/noworneverev/leetcode-api/main/data/leetcode_questions.json"
)


def folder_name(number: int, title_slug: str) -> str:
    return f"{number:04d}_{title_slug.replace('-', '_')}"


def load_json(path: Path, default=None):
    if not path.exists():
        return default
    with path.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def save_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    temp_path.replace(path)


def download_neenza(cache_path: Path, force_refresh: bool) -> dict[str, dict]:
    if cache_path.exists() and not force_refresh:
        payload = load_json(cache_path)
        if isinstance(payload, dict) and "questions" in payload:
            return {item["frontend_id"]: item for item in payload["questions"]}

    with urllib.request.urlopen(NEENZA_URL, timeout=180) as response:
        payload = json.load(response)

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with cache_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False)

    return {item["frontend_id"]: item for item in payload["questions"]}


def load_questions(repo_root: Path, force_refresh: bool) -> dict[str, dict]:
    cache_path = repo_root / "config" / "questions-full.json"
    if cache_path.exists() and not force_refresh:
        payload = load_json(cache_path)
    else:
        with urllib.request.urlopen(DEFAULT_QUESTIONS_URL, timeout=180) as response:
            payload = json.load(response)
        save_json(cache_path, payload)

    return {
        entry["data"]["question"]["questionFrontendId"]: entry["data"]["question"]
        for entry in payload
    }


def normalize_cases(raw_cases: list[dict]) -> list[dict]:
    normalized: list[dict] = []
    for case in raw_cases:
        kind = case.get("kind")
        if kind == "design":
            normalized.append(
                {
                    "kind": "design",
                    "operations": case["operations"],
                    "arguments": case["arguments"],
                    "expected": case["expected"],
                }
            )
            continue
        if kind == "sql":
            normalized.append(
                {
                    "kind": "sql",
                    "tables": case["tables"],
                    "expected": case["expected"],
                }
            )
            continue
        if kind == "shell":
            normalized.append(
                {
                    "kind": "shell",
                    "file": case.get("file", "input.txt"),
                    "input": case["input"],
                    "expected": case["expected"],
                }
            )
            continue
        if kind == "pandas":
            normalized.append(
                {
                    "kind": "pandas",
                    "args": case["args"],
                    "expected": case["expected"],
                }
            )
            continue

        if "args" in case:
            normalized.append({"args": case["args"], "expected": case["expected"]})
        elif "input" in case:
            normalized.append({"input": case["input"], "expected": case["expected"]})
        else:
            normalized.append(case)
    return normalized


PANDAS_PROBLEM_NUMBERS = set(range(2877, 2892))


def extract_cases_for_question(
    number: int,
    question: dict,
    neenza_by_id: dict[str, dict],
    readme_path: Path | None,
    *,
    prefer_sql_from_readme: bool = False,
    prefer_pandas_from_readme: bool = False,
) -> tuple[list[dict], dict | None]:
    frontend_id = str(number)
    neenza = neenza_by_id.get(frontend_id)

    if prefer_pandas_from_readme and readme_path and readme_path.exists():
        readme = readme_path.read_text(encoding="utf-8-sig")
        from pandas_parser import parse_pandas_examples_from_markdown  # noqa: WPS433

        pandas_cases = parse_pandas_examples_from_markdown(readme)
        if pandas_cases:
            return normalize_cases(pandas_cases), metadata_from_neenza(neenza)

    if prefer_sql_from_readme and readme_path and readme_path.exists():
        readme = readme_path.read_text(encoding="utf-8-sig")
        readme_cases = parse_examples_from_markdown(readme)
        sql_cases = [case for case in readme_cases if case.get("kind") == "sql"]
        if sql_cases:
            return normalize_cases(sql_cases), None

    raw_cases: list[dict] = []
    metadata = None

    if neenza:
        for example in neenza.get("examples", []):
            parsed = parse_example_text(example.get("example_text", ""))
            if parsed:
                raw_cases.append(parsed)
        metadata = metadata_from_neenza(neenza)

    if not raw_cases:
        raw_cases = parse_examples_from_html(question.get("content") or "")

    if not raw_cases and readme_path and readme_path.exists():
        readme = readme_path.read_text(encoding="utf-8-sig")
        raw_cases = parse_examples_from_markdown(readme)

    if not raw_cases:
        title = question.get("title", "")
        try:
            from doocs_fetcher import fetch_doocs_readme_en  # noqa: WPS433

            doocs_md = fetch_doocs_readme_en(number, title)
            if doocs_md:
                raw_cases = parse_examples_from_markdown(doocs_md)
        except Exception:
            pass

    return normalize_cases(raw_cases), metadata


def should_skip_override(number: int, protected: set[str]) -> bool:
    return str(number) in protected


def load_problem_tags(repo_root: Path) -> dict[int, str]:
    problems_path = repo_root / "config" / "problems.json"
    if not problems_path.exists():
        return {}
    payload = load_json(problems_path, default=[]) or []
    return {int(item["Number"]): str(item.get("Tags") or "") for item in payload}


def is_legacy_sql_case(cases: list[dict]) -> bool:
    if not cases:
        return False
    first = cases[0]
    if first.get("kind") == "sql":
        return False
    inputs = first.get("input")
    if inputs is None:
        return False
    values = inputs if isinstance(inputs, list) else [inputs]
    return any("table:" in str(value).lower() for value in values)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--number", type=int, help="Sync a single problem number")
    parser.add_argument("--tag", help="Only sync problems whose Tags contain this value (e.g. database, shell)")
    parser.add_argument("--legacy-sql-only", action="store_true", help="Only resync legacy SQL-shaped cases")
    parser.add_argument("--force", action="store_true", help="Overwrite existing non-empty cases")
    parser.add_argument("--force-refresh", action="store_true", help="Re-download source datasets")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo_root = args.repo_root
    neenza_by_id = download_neenza(repo_root / "config" / "neenza-problems.json", args.force_refresh)
    questions = load_questions(repo_root, args.force_refresh)
    overrides = load_json(repo_root / "config" / "problem-test-overrides.json", default={}) or {}
    protected = set(overrides.keys())
    tags_by_number = load_problem_tags(repo_root)

    targets = questions.items()
    if args.number is not None:
        targets = [(str(args.number), questions[str(args.number)])]

    updated = 0
    skipped = 0
    empty = 0
    missing_folder = 0

    for frontend_id, question in targets:
        number = int(frontend_id)
        if args.tag:
            tag_line = tags_by_number.get(number, "")
            if args.tag not in tag_line.split(","):
                skipped += 1
                continue
        if should_skip_override(number, protected):
            skipped += 1
            continue

        title_slug = question.get("url", "").rstrip("/").split("/")[-1]
        if not title_slug:
            continue

        problem_dir = repo_root / folder_name(number, title_slug)
        tests_dir = problem_dir / "tests"
        if not tests_dir.exists():
            missing_folder += 1
            continue

        cases_path = tests_dir / "cases.json"
        config_path = tests_dir / "config.json"
        existing_cases_doc = load_json(cases_path, default={"cases": []}) or {"cases": []}
        existing_config = load_json(config_path, default={}) or {}
        existing_cases = existing_cases_doc.get("cases") or []

        if args.legacy_sql_only and not is_legacy_sql_case(existing_cases):
            skipped += 1
            continue

        if existing_cases and not args.force:
            skipped += 1
            continue

        cases, metadata = extract_cases_for_question(
            number,
            question,
            neenza_by_id,
            problem_dir / "README.md",
            prefer_sql_from_readme=bool(
                args.tag == "database"
                or args.legacy_sql_only
                or "database" in tags_by_number.get(number, "").split(",")
            ),
            prefer_pandas_from_readme=number in PANDAS_PROBLEM_NUMBERS,
        )

        if not cases:
            empty += 1
            continue

        config = build_config(existing_config, metadata, cases)
        cases_doc = {"cases": cases}

        if args.dry_run:
            print(f"DRY {problem_dir.name}: {len(cases)} cases, method={config.get('method')}")
            updated += 1
            continue

        save_json(cases_path, cases_doc)
        save_json(config_path, config)
        updated += 1

        if updated % 250 == 0:
            print(f"Updated {updated} problems...")

    print(
        f"Done. updated={updated}, skipped={skipped}, no_examples={empty}, missing_folder={missing_folder}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
