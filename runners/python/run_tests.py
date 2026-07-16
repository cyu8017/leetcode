#!/usr/bin/env python3
"""Run tests for a LeetCode Python solution."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

RUNNERS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RUNNERS_DIR / "common"))

from test_utils import load_problem_tests, run_cases, run_design_cases, uses_design_cases  # noqa: E402
from runner_policy import EXIT_CONFIG, EXIT_NO_CASES, pre_run_check, print_skip  # noqa: E402


def load_solution_module(problem_dir: Path):
    solution_path = problem_dir / "solution.py"
    spec = importlib.util.spec_from_file_location("leetcode_solution", solution_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {solution_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: run_tests.py <problem_dir>")
        return 2

    problem_dir = Path(sys.argv[1]).resolve()
    config, cases_doc = load_problem_tests(problem_dir)
    can_run, exit_code, message = pre_run_check(
        "python",
        config,
        cases_doc,
        has_solution_file=(problem_dir / "solution.py").exists(),
    )
    if not can_run:
        print(f"Python tests: {problem_dir.name}")
        print_skip(message)
        return exit_code

    module = load_solution_module(problem_dir)

    if uses_design_cases(cases_doc) or config.get("kind") == "design":
        design_class = config.get("class") or cases_doc["cases"][0]["operations"][0]
        print(f"Python design tests: {problem_dir.name} :: {design_class}")
        passed, total = run_design_cases(module, cases_doc)
        print(f"Result: {passed}/{total} passed")
        return 0 if passed == total else 1

    if config.get("class") in {"ZigzagIterator", "NestedIterator"}:
        print(f"Python tests: {problem_dir.name} :: {config['class']}")
        passed, total = run_cases(None, config, cases_doc, module)
    else:
        solution_class = getattr(module, config.get("class", "Solution"))
        solution = solution_class()
        print(f"Python tests: {problem_dir.name} :: {config['method']}()")
        passed, total = run_cases(solution, config, cases_doc, module)
    print(f"Result: {passed}/{total} passed")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
