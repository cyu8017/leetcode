"""Shared exit-code policy for all language test runners."""

from __future__ import annotations

from typing import Any

EXIT_OK = 0
EXIT_FAIL = 1
EXIT_CONFIG = 2
EXIT_NO_CASES = 4

DESIGN_NATIVE_LANGUAGES = frozenset({"python", "javascript", "typescript", "java"})
COMPILED_LANGUAGES = frozenset({"cpp", "c", "go", "rust", "kotlin", "csharp", "scala", "swift"})
UNSUPPORTED_KINDS = frozenset({"sql", "shell", "pandas"})


def resolve_kind(config: dict[str, Any], cases_doc: dict[str, Any]) -> str:
    if config.get("kind"):
        return str(config["kind"])
    cases = cases_doc.get("cases") or []
    if cases and cases[0].get("kind"):
        return str(cases[0]["kind"])
    return "standard"


def pre_run_check(
    language: str,
    config: dict[str, Any],
    cases_doc: dict[str, Any],
    *,
    has_solution_file: bool = True,
    has_python_reference: bool = False,
    toolchain_available: bool = True,
) -> tuple[bool, int, str]:
    cases = cases_doc.get("cases") or []
    if not cases:
        return False, EXIT_NO_CASES, "no test cases defined in tests/cases.json"

    kind = resolve_kind(config, cases_doc)

    if kind in UNSUPPORTED_KINDS:
        if config.get("runnable") is False:
            return False, EXIT_OK, f"SKIP kind={kind} (runner not implemented)"
        return False, EXIT_CONFIG, f"kind={kind} requires a runner but none is configured"

    if kind == "design":
        if language in DESIGN_NATIVE_LANGUAGES:
            if not has_solution_file:
                return False, EXIT_CONFIG, f"missing solution file for {language}"
            if not toolchain_available:
                return False, EXIT_CONFIG, f"{language} toolchain not available"
            return True, EXIT_OK, ""
        if language in COMPILED_LANGUAGES:
            if not has_python_reference:
                return False, EXIT_CONFIG, "design problems require a Python reference implementation"
            return True, EXIT_OK, ""
        return False, EXIT_CONFIG, f"design cases not supported for language={language}"

    if not has_solution_file:
        return False, EXIT_CONFIG, f"missing solution file for {language}"

    if not toolchain_available:
        return False, EXIT_CONFIG, f"{language} toolchain not available"

    return True, EXIT_OK, ""


def print_skip(message: str) -> None:
    print(f"  {message}")


def is_stub_method(config: dict[str, Any]) -> bool:
    return config.get("method") == "solve" and config.get("kind") not in UNSUPPORTED_KINDS
