"""Parse LeetCode pandas study-plan examples from README markdown."""

from __future__ import annotations

import re
from typing import Any

from example_parser import _normalize_example_text, _parse_assignment, _parse_value, _split_top_level_commas
from sql_shell_parser import parse_ascii_table


def parse_pandas_example_chunk(chunk: str) -> dict[str, Any] | None:
    text = _normalize_example_text(chunk)
    if "dataframe" not in text.lower() and "student_data" not in text.lower():
        return None

    input_match = re.search(r"Input:?\s*(.*)", text, flags=re.IGNORECASE | re.DOTALL)
    if not input_match:
        return None

    remainder = input_match.group(1)
    output_match = re.search(r"Output:?\s*(.*)", remainder, flags=re.IGNORECASE | re.DOTALL)
    if not output_match:
        return None

    input_text = remainder[: output_match.start()]
    output_text = output_match.group(1)
    explanation_match = re.search(r"Explanation:?\s*", output_text, flags=re.IGNORECASE)
    if explanation_match:
        output_text = output_text[: explanation_match.start()]

    args: dict[str, Any] = {}
    cleaned_input = re.sub(r"\*+", "", input_text)
    for segment in _split_top_level_commas(cleaned_input.replace("\n", " ")):
        name, value = _parse_assignment(segment.strip())
        if name:
            args[name] = value

    if not args:
        return None

    expected_rows = parse_ascii_table(output_text)
    if not expected_rows:
        return None

    return {"kind": "pandas", "args": args, "expected": expected_rows}


def parse_pandas_examples_from_markdown(problem_md: str) -> list[dict[str, Any]]:
    if not problem_md or "dataframe" not in problem_md.lower():
        return []

    section_match = re.search(r"## Problem\s*\n+(.*?)(?:\n## |\Z)", problem_md, flags=re.DOTALL)
    body = section_match.group(1) if section_match else problem_md

    cases: list[dict[str, Any]] = []
    for block in re.findall(r"```(?:\n|\r\n?)(.*?)```", body, flags=re.DOTALL):
        parsed = parse_pandas_example_chunk(block)
        if parsed:
            cases.append(parsed)

    if not cases:
        example_chunks = re.split(r"\*\*Example\s*\d*:?\s*\*\*", body, flags=re.IGNORECASE)
        for chunk in example_chunks[1:]:
            parsed = parse_pandas_example_chunk(chunk)
            if parsed:
                cases.append(parsed)

    return cases
