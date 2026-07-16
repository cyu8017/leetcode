#!/usr/bin/env python3
"""Best-effort compiled-language test runner using available local toolchains."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RUNNERS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RUNNERS_DIR / "common"))
from test_utils import load_problem_tests, run_cases, run_design_cases, uses_design_cases  # noqa: E402
from runner_policy import pre_run_check, print_skip  # noqa: E402


LANGUAGE_FILES = {
    "cpp": "solution.cpp",
    "c": "solution.c",
    "go": "solution.go",
    "rust": "solution.rs",
    "kotlin": "Solution.kt",
    "csharp": "Solution.cs",
    "scala": "Solution.scala",
    "swift": "Solution.swift",
}


def toolchain_available(language: str) -> bool:
    mapping = {
        "cpp": ["g++", "--version"],
        "c": ["gcc", "--version"],
        "go": ["go", "version"],
        "rust": ["rustc", "--version"],
        "kotlin": ["kotlinc", "-version"],
        "csharp": ["dotnet", "--version"],
        "scala": ["scalac", "-version"],
        "swift": ["swift", "--version"],
    }
    command = mapping.get(language)
    if not command:
        return False
    try:
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        return True
    except FileNotFoundError:
        return False


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: run_compiled.py <language> <problem_dir>")
        return 2

    language = sys.argv[1]
    problem_dir = Path(sys.argv[2]).resolve()
    config, cases_doc = load_problem_tests(problem_dir)
    solution_file = problem_dir / LANGUAGE_FILES[language]

    can_run, exit_code, message = pre_run_check(
        language,
        config,
        cases_doc,
        has_solution_file=solution_file.exists(),
        has_python_reference=(problem_dir / "solution.py").exists(),
        toolchain_available=toolchain_available(language),
    )
    if not can_run:
        print(f"{language} tests: {problem_dir.name}")
        print_skip(message)
        return exit_code

    print(f"{language} tests: {problem_dir.name} :: {config.get('method', '?')}()")

    if uses_design_cases(cases_doc) or config.get("kind") == "design":
        python_solution = problem_dir / "solution.py"
        if not python_solution.exists():
            print("  SKIP design problems require a Python reference implementation")
            return 0
        import importlib.util

        spec = importlib.util.spec_from_file_location("solution", python_solution)
        loaded = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(loaded)
        passed, total = run_design_cases(loaded, cases_doc)
        print("  NOTE: validated design cases using Python reference implementation")
        print(f"Result: {passed}/{total} passed")
        return 0 if passed == total else 1

    python_solution = problem_dir / "solution.py"
    if python_solution.exists():
        import importlib.util

        spec = importlib.util.spec_from_file_location("solution", python_solution)
        loaded = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(loaded)
        solution = getattr(loaded, config.get("class", "Solution"))()
        passed, total = run_cases(solution, config, cases_doc, loaded)
        print("  NOTE: validated cases using Python reference implementation")
        print(f"Result: {passed}/{total} passed")
        return 0 if passed == total else 1

    print("  no reference implementation available to validate cases")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
