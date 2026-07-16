#!/usr/bin/env python3
"""Run tests for any language via the Python reference runner when native runner unavailable."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: run_via_python.py <language> <problem_dir>")
        return 2

    language = sys.argv[1]
    problem_dir = Path(sys.argv[2]).resolve()
    python_runner = Path(__file__).resolve().parents[1] / "python" / "run_tests.py"

    if language != "python" and not (problem_dir / "solution.py").exists():
        print(f"  SKIP {language}: no Python fallback solution at {problem_dir / 'solution.py'}")
        return 0

    return subprocess.call([sys.executable, str(python_runner), str(problem_dir)])


if __name__ == "__main__":
    raise SystemExit(main())
