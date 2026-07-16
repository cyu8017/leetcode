"""Parse SQL and Shell LeetCode examples from README markdown."""

from __future__ import annotations

import html
import re
from typing import Any


def _coerce_cell(value: str) -> Any:
    value = html.unescape(value.strip())
    if not value or value.lower() == "null":
        return None
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def parse_ascii_table(text: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    header: list[str] | None = None

    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        if set(line.replace("|", "").replace("-", "").replace("+", "").strip()) <= {" "}:
            continue
        if re.fullmatch(r"\|[\s\-\+|]+\|", line):
            continue

        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if len(cells) != len(header):
            continue
        rows.append({header[index]: _coerce_cell(value) for index, value in enumerate(cells)})

    return rows


def _parse_bare_table_section(section_text: str) -> dict[str, list[dict[str, Any]]]:
    tables: dict[str, list[dict[str, Any]]] = {}
    lines = section_text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if re.fullmatch(r"[A-Za-z_]\w*", line) and line.lower() not in {"input", "output", "explanation"}:
            table_name = line
            index += 1
            block_lines: list[str] = []
            while index < len(lines):
                next_line = lines[index].strip()
                if re.fullmatch(r"[A-Za-z_]\w*", next_line) and next_line.lower() not in {
                    "input",
                    "output",
                    "explanation",
                }:
                    break
                block_lines.append(lines[index])
                index += 1
            rows = parse_ascii_table("\n".join(block_lines))
            if rows:
                tables[table_name] = rows
            continue
        index += 1
    return tables


def _parse_sql_section(section_text: str) -> dict[str, list[dict[str, Any]]]:
    tables: dict[str, list[dict[str, Any]]] = {}
    pattern = re.compile(r"([`\"']?)([A-Za-z_][\w]*)\1\s+table:\s*", flags=re.IGNORECASE)
    matches = list(pattern.finditer(section_text))
    if not matches:
        return _parse_bare_table_section(section_text)

    for index, match in enumerate(matches):
        table_name = match.group(2)
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section_text)
        block = section_text[start:end].strip()
        rows = parse_ascii_table(block)
        if rows:
            tables[table_name] = rows
    if not tables:
        return _parse_bare_table_section(section_text)
    return tables


def parse_sql_example_chunk(chunk: str) -> dict[str, Any] | None:
    from example_parser import _normalize_example_text  # noqa: WPS433

    chunk = _normalize_example_text(re.sub(r"```[^\n]*\n|```", "", chunk.strip()))
    if "table:" not in chunk.lower() and not re.search(
        r"(?:^|\n)[A-Za-z_]\w*\s*\n\+",
        chunk,
        flags=re.MULTILINE,
    ):
        return None

    input_match = re.search(r"Input:?\s*(.*)", chunk, flags=re.IGNORECASE | re.DOTALL)
    if not input_match:
        return None

    remainder = input_match.group(1)
    output_match = re.search(r"Output:?\s*(.*)", remainder, flags=re.IGNORECASE | re.DOTALL)
    if not output_match:
        return None

    input_text = remainder[: output_match.start()]
    output_and_rest = output_match.group(1)
    explanation_match = re.search(r"Explanation:?\s*", output_and_rest, flags=re.IGNORECASE)
    output_text = output_and_rest[: explanation_match.start()] if explanation_match else output_and_rest

    tables = _parse_sql_section(input_text)
    expected = parse_ascii_table(output_text)
    if not tables or not expected:
        return None

    return {"kind": "sql", "tables": tables, "expected": expected}


def parse_sql_examples_from_markdown(problem_md: str) -> list[dict[str, Any]]:
    section_match = re.search(r"## Problem\s*\n+(.*?)(?:\n## |\Z)", problem_md, flags=re.DOTALL)
    body = section_match.group(1) if section_match else problem_md
    body = re.sub(r"_Problem text from.*", "", body, flags=re.DOTALL)

    if "table:" not in body.lower() and "Table:" not in body:
        return []

    cases: list[dict[str, Any]] = []
    chunks = re.split(r"\*\*Example\s*\d*:?\s*\*\*", body, flags=re.IGNORECASE)
    for chunk in chunks[1:]:
        parsed = parse_sql_example_chunk(chunk)
        if parsed:
            cases.append(parsed)

    if not cases:
        parsed = parse_sql_example_chunk(body)
        if parsed:
            cases.append(parsed)
    return cases


def parse_shell_examples_from_markdown(problem_md: str) -> list[dict[str, Any]]:
    section_match = re.search(r"## Problem\s*\n+(.*?)(?:\n## |\Z)", problem_md, flags=re.DOTALL)
    body = section_match.group(1) if section_match else problem_md

    file_match = re.search(r"`([\w.-]+\.txt)`", body)
    filename = file_match.group(1) if file_match else "input.txt"

    content_idx = body.lower().find("content")
    output_markers = ["which is:", "output the following", "should output", "expected output", "output:"]
    output_idx = -1
    for marker in output_markers:
        idx = body.lower().find(marker)
        if idx != -1:
            output_idx = idx
            break
    if content_idx == -1 or output_idx == -1 or output_idx <= content_idx:
        return []

    input_text = None
    expected_text = None
    for match in re.finditer(r"```[^\n]*\n(.*?)```", body, flags=re.DOTALL):
        if match.start() > content_idx and match.start() < output_idx:
            input_text = match.group(1).rstrip("\n")
        elif match.start() > output_idx:
            expected_text = match.group(1).rstrip("\n")
            break

    if not input_text or not expected_text:
        return []

    return [
        {
            "kind": "shell",
            "file": filename,
            "input": input_text,
            "expected": expected_text,
        }
    ]
