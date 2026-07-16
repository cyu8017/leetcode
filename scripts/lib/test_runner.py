"""Shared local/Docker test dispatch for batch runners."""

from __future__ import annotations

import subprocess
from pathlib import Path

RUNNERS = {
    "python": ("python", "runners/python/run_tests.py"),
    "javascript": ("node", "runners/javascript/run_tests.mjs"),
    "typescript": ("node", "runners/typescript/run_tests.mjs"),
    "java": ("python", "runners/java/run_tests.py"),
    "ruby": ("ruby", "runners/ruby/run_tests.rb"),
    "php": ("php", "runners/php/run_tests.php"),
    "cpp": ("python", "runners/cpp/run_tests.py"),
    "c": ("python", "runners/compiled/run_compiled.py", "c"),
    "go": ("python", "runners/compiled/run_compiled.py", "go"),
    "rust": ("python", "runners/compiled/run_compiled.py", "rust"),
    "kotlin": ("python", "runners/compiled/run_compiled.py", "kotlin"),
    "csharp": ("python", "runners/compiled/run_compiled.py", "csharp"),
    "scala": ("python", "runners/compiled/run_compiled.py", "scala"),
    "swift": ("python", "runners/compiled/run_compiled.py", "swift"),
}


def run_local(repo_root: Path, folder: str, language: str) -> int:
    runner = RUNNERS.get(language)
    if not runner:
        print(f"Unknown language: {language}")
        return 2

    problem_dir = repo_root / folder
    if not problem_dir.exists():
        print(f"Missing folder: {folder}")
        return 2

    command = list(runner) + [str(problem_dir)]
    print(f"\n==> {folder} :: {language} (local)", flush=True)
    result = subprocess.run(command, cwd=repo_root)
    return result.returncode


def run_docker(repo_root: Path, folder: str, language: str) -> int:
    compose_file = repo_root / "docker" / "docker-compose.yml"
    print(f"\n==> {folder} :: {language} (Docker)", flush=True)
    result = subprocess.run(
        [
            "docker",
            "compose",
            "-f",
            str(compose_file),
            "run",
            "--rm",
            language,
            language,
            folder,
        ],
        cwd=repo_root,
    )
    return result.returncode
