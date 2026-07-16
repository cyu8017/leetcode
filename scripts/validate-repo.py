#!/usr/bin/env python3
"""Validate problem folders, test configs, and cases.json schema."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "lib"))
sys.path.insert(0, str(SCRIPT_DIR.parent / "runners" / "common"))

from runner_policy import UNSUPPORTED_KINDS, resolve_kind  # noqa: E402

FOLDER_PATTERN = re.compile(r"^(\d{4})_[a-z0-9_]+$")
README_PLACEHOLDER = "_Problem description unavailable"
PREMIUM_PLACEHOLDER = "LeetCode Premium"


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checked: int = 0

    def error(self, folder: str, message: str) -> None:
        self.errors.append(f"{folder}: {message}")

    def warn(self, folder: str, message: str) -> None:
        self.warnings.append(f"{folder}: {message}")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def validate_standard_case(folder: str, index: int, case: dict, report: ValidationReport) -> None:
    if "expected" not in case:
        report.error(folder, f"case {index}: missing expected")
    if "args" not in case and "input" not in case:
        report.error(folder, f"case {index}: missing args or input")


def validate_design_case(folder: str, index: int, case: dict, report: ValidationReport) -> None:
    for key in ("operations", "arguments", "expected"):
        if key not in case:
            report.error(folder, f"design case {index}: missing {key}")
            return
    if case["operations"] and not isinstance(case["operations"][0], str):
        report.error(folder, f"design case {index}: operations[0] must be class name string")


def validate_sql_case(folder: str, index: int, case: dict, report: ValidationReport) -> None:
    for key in ("tables", "expected"):
        if key not in case:
            report.error(folder, f"sql case {index}: missing {key}")


def validate_shell_case(folder: str, index: int, case: dict, report: ValidationReport) -> None:
    for key in ("input", "expected"):
        if key not in case:
            report.error(folder, f"shell case {index}: missing {key}")


def validate_pandas_case(folder: str, index: int, case: dict, report: ValidationReport) -> None:
    for key in ("args", "expected"):
        if key not in case:
            report.error(folder, f"pandas case {index}: missing {key}")


def validate_cases(folder: str, cases_doc: dict, report: ValidationReport) -> str | None:
    cases = cases_doc.get("cases")
    if cases is None:
        report.error(folder, "cases.json missing cases array")
        return None
    if not isinstance(cases, list):
        report.error(folder, "cases must be an array")
        return None

    kinds = {case.get("kind", "standard") for case in cases}
    if len(kinds) > 1:
        report.error(folder, f"mixed case kinds in one file: {sorted(kinds)}")

    kind = next(iter(kinds)) if kinds else "standard"
    if kind == "standard" and kinds == {"standard"}:
        kind = "standard"

    for index, case in enumerate(cases, start=1):
        case_kind = case.get("kind", kind if kind != "standard" else "standard")
        if case_kind == "design":
            validate_design_case(folder, index, case, report)
        elif case_kind == "sql":
            validate_sql_case(folder, index, case, report)
        elif case_kind == "shell":
            validate_shell_case(folder, index, case, report)
        elif case_kind == "pandas":
            validate_pandas_case(folder, index, case, report)
        else:
            validate_standard_case(folder, index, case, report)

    if kind == "standard" and cases:
        return "standard"
    return kind if cases else None


def validate_config(
    folder: str,
    config: dict,
    cases_doc: dict,
    case_kind: str | None,
    report: ValidationReport,
) -> None:
    resolved = resolve_kind(config, cases_doc)
    if case_kind and resolved != case_kind and case_kind != "standard":
        report.error(folder, f"config kind={resolved!r} does not match cases kind={case_kind!r}")

    if resolved == "design":
        if not config.get("class"):
            report.error(folder, "design config missing class")
        if config.get("method"):
            report.warn(folder, "design config should not set method")
        return

    if resolved in UNSUPPORTED_KINDS:
        if config.get("runnable") is not False:
            report.warn(folder, f"kind={resolved} should set runnable=false until runner exists")
        return

    if not config.get("method"):
        report.error(folder, "standard config missing method")
    elif config.get("method") == "solve" and cases_doc.get("cases"):
        has_param_order = bool(config.get("paramOrder"))
        kind = resolve_kind(config, cases_doc)
        if not has_param_order and kind not in UNSUPPORTED_KINDS:
            report.warn(folder, "config still uses placeholder method=solve")


def validate_readme(folder: str, readme_path: Path, report: ValidationReport) -> None:
    if not readme_path.exists():
        report.warn(folder, "missing README.md")
        return
    text = readme_path.read_text(encoding="utf-8-sig")
    if README_PLACEHOLDER in text:
        report.warn(folder, "README still has unavailable placeholder text")
    if text.strip().endswith(PREMIUM_PLACEHOLDER) or "> **LeetCode Premium**" in text[:400]:
        return
    if len(text.strip()) < 80:
        report.warn(folder, "README looks unusually short")


def validate_problem_dir(
    problem_dir: Path,
    known_numbers: set[int],
    report: ValidationReport,
) -> None:
    folder = problem_dir.name
    report.checked += 1

    match = FOLDER_PATTERN.match(folder)
    if not match:
        report.error(folder, "folder name must match NNNN_snake_case_title")
        return

    number = int(match.group(1))
    if number not in known_numbers:
        report.warn(folder, "problem number not found in config/problems.json")

    tests_dir = problem_dir / "tests"
    cases_path = tests_dir / "cases.json"
    config_path = tests_dir / "config.json"

    if not tests_dir.is_dir():
        report.error(folder, "missing tests/ directory")
        return
    if not cases_path.exists():
        report.error(folder, "missing tests/cases.json")
        return
    if not config_path.exists():
        report.error(folder, "missing tests/config.json")
        return

    try:
        cases_doc = load_json(cases_path)
        config = load_json(config_path)
    except json.JSONDecodeError as exc:
        report.error(folder, f"invalid JSON: {exc}")
        return

    case_kind = validate_cases(folder, cases_doc, report)
    validate_config(folder, config, cases_doc, case_kind, report)
    validate_readme(folder, problem_dir / "README.md", report)


def load_known_numbers(repo_root: Path) -> set[int]:
    problems_path = repo_root / "config" / "problems.json"
    if not problems_path.exists():
        return set()
    problems = load_json(problems_path)
    return {int(item["Number"]) for item in problems}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=SCRIPT_DIR.parent)
    parser.add_argument("--folder", help="Validate one folder only")
    parser.add_argument("--warnings-as-errors", action="store_true")
    parser.add_argument("--limit", type=int, help="Validate first N folders (debug)")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    report = ValidationReport()
    known_numbers = load_known_numbers(repo_root)

    if args.folder:
        targets = [repo_root / args.folder]
    else:
        targets = sorted(
            path for path in repo_root.iterdir() if path.is_dir() and FOLDER_PATTERN.match(path.name)
        )
        if args.limit:
            targets = targets[: args.limit]

    for problem_dir in targets:
        validate_problem_dir(problem_dir, known_numbers, report)

    print(f"Checked {report.checked} problem folder(s)")
    print(f"Errors: {len(report.errors)}")
    print(f"Warnings: {len(report.warnings)}")

    for message in report.errors[:50]:
        print(f"ERROR  {message}")
    if len(report.errors) > 50:
        print(f"... and {len(report.errors) - 50} more errors")

    for message in report.warnings[:20]:
        print(f"WARN   {message}")
    if len(report.warnings) > 20:
        print(f"... and {len(report.warnings) - 20} more warnings")

    output_path = repo_root / "config" / "last-validation.json"
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "checked": report.checked,
                "errorCount": len(report.errors),
                "warningCount": len(report.warnings),
                "errors": report.errors,
                "warnings": report.warnings,
            },
            handle,
            indent=2,
        )
    print(f"Report: {output_path.relative_to(repo_root)}")

    if report.errors:
        return 1
    if args.warnings_as_errors and report.warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
