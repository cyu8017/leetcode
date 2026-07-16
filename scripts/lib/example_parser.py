"""Parse LeetCode example Input/Output text into structured test cases."""

from __future__ import annotations

import ast
import json
import re
from typing import Any


def _normalize_example_text(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\*\*Input:\s*\n\*\*", "Input:\n", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*Output:\s*\n\*\*", "Output:\n", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*Explanation:\s*\n\*\*", "Explanation:\n", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*Input:?\s*\*\*", "Input:", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*Output:?\s*\*\*", "Output:", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*Explanation:?\s*\*\*", "Explanation:", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*Input:?\*\*", "Input:", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*Output:?\*\*", "Output:", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*Explanation:?\*\*", "Explanation:", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*Input:?\s*", "Input:", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*Output:?\s*", "Output:", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*Explanation:?\s*", "Explanation:", text, flags=re.IGNORECASE)
    text = re.sub(r"(\w+):\*\*", r"\1:", text)
    text = re.sub(r"\*\*\[", "[", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()


def _parse_value(raw: str) -> Any:
    value = raw.strip().rstrip(",")
    if not value:
        return value
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in {"null", "none"}:
        return None
    if value == "...":
        return "..."

    for parser in (_json_load, ast.literal_eval):
        try:
            parsed = parser(value)
            return _sanitize_parsed(parsed)
        except (ValueError, SyntaxError, json.JSONDecodeError):
            continue

    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def _sanitize_parsed(value: Any) -> Any:
    if value is Ellipsis:
        return "..."
    if isinstance(value, list):
        return [_sanitize_parsed(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize_parsed(item) for item in value]
    if isinstance(value, dict):
        return {key: _sanitize_parsed(item) for key, item in value.items()}
    return value


def _json_load(value: str) -> Any:
    return json.loads(value)


def _split_top_level_commas(text: str) -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    depth = 0
    in_string: str | None = None
    escape = False

    for char in text:
        if in_string:
            current.append(char)
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == in_string:
                in_string = None
            continue

        if char in "\"'":
            in_string = char
            current.append(char)
            continue

        if char in "[({":
            depth += 1
        elif char in "])}":
            depth -= 1

        if char == "," and depth == 0:
            part = "".join(current).strip()
            if part:
                parts.append(part)
            current = []
            continue

        current.append(char)

    tail = "".join(current).strip()
    if tail:
        parts.append(tail)
    return parts


def _parse_assignment(segment: str) -> tuple[str | None, Any]:
    segment = segment.strip()
    match = re.match(r"^([A-Za-z_]\w*)\s*=\s*(.+)$", segment, flags=re.DOTALL)
    if match:
        return match.group(1), _parse_value(match.group(2))
    match = re.match(r"^([A-Za-z_]\w*)\s*:\s*(.+)$", segment, flags=re.DOTALL)
    if match:
        return match.group(1), _parse_value(match.group(2))
    return None, _parse_value(segment)


def _parse_input_block(input_text: str) -> dict[str, Any] | list[Any] | Any:
    input_text = input_text.strip()
    if not input_text:
        return {}

    lines = [line.strip() for line in input_text.split("\n") if line.strip()]

    json_lines = [line for line in lines if line.startswith("[")]
    if len(json_lines) >= 2:
        operations = _parse_value(json_lines[0])
        arguments = _parse_value(json_lines[1])
        if (
            isinstance(operations, list)
            and operations
            and all(isinstance(item, str) for item in operations)
            and isinstance(arguments, list)
        ):
            return {"operations": operations, "arguments": arguments}

    if len(lines) == 1 and "=" not in lines[0] and lines[0].startswith(("[", "{", '"', "'")):
        return _parse_value(lines[0])

    if len(lines) >= 2 and lines[0].startswith("["):
        operations = _parse_value(lines[0])
        if len(lines) == 2:
            arguments = _parse_value(lines[1])
            if not isinstance(arguments, list):
                arguments = [arguments]
            return {"operations": operations, "arguments": arguments}

        return {
            "operations": operations,
            "arguments": [_parse_value(line) for line in lines[1:]],
        }

    joined = " ".join(lines)
    if "=" not in joined and joined.startswith(("[", "{")):
        return _parse_value(joined)

    args: dict[str, Any] = {}
    positional: list[Any] = []
    for segment in _split_top_level_commas(joined):
        name, value = _parse_assignment(segment)
        if name:
            args[name] = value
        else:
            positional.append(value)

    if args:
        return args
    if len(positional) == 1:
        return positional[0]
    return {"_positional": positional}


def _parse_output_block(output_text: str) -> Any:
    output_text = output_text.strip()
    if not output_text:
        return None
    lines = [line.strip() for line in output_text.split("\n") if line.strip()]
    if len(lines) == 1:
        return _parse_value(lines[0])
    if lines[0].startswith("["):
        return _parse_value("\n".join(lines))
    return _parse_value(lines[0])


def parse_example_text(example_text: str) -> dict[str, Any] | None:
    text = _normalize_example_text(example_text)
    if not text:
        return None

    input_match = re.search(r"Input:?\s*(.*)", text, flags=re.IGNORECASE | re.DOTALL)
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

    parsed_input = _parse_input_block(input_text)
    expected = _parse_output_block(output_text)

    if isinstance(parsed_input, dict) and "operations" in parsed_input:
        ops = parsed_input["operations"]
        if isinstance(ops, list) and ops and all(isinstance(item, str) for item in ops):
            return {
                "kind": "design",
                "operations": ops,
                "arguments": parsed_input.get("arguments", []),
                "expected": expected,
            }

    if isinstance(parsed_input, dict) and "_positional" not in parsed_input and parsed_input:
        return {"args": parsed_input, "expected": expected}

    if isinstance(parsed_input, list):
        return {"input": parsed_input, "expected": expected}

    return {"input": [parsed_input], "expected": expected}


def parse_examples_from_html(content: str) -> list[dict[str, Any]]:
    if not content:
        return []

    import html as html_module

    cases: list[dict[str, Any]] = []
    for block in re.findall(r"<pre>\s*(.*?)\s*</pre>", content, flags=re.IGNORECASE | re.DOTALL):
        text = html_module.unescape(re.sub(r"<[^>]+>", "", block))
        parsed = parse_example_text(text)
        if parsed:
            cases.append(parsed)
    return cases


def parse_examples_from_markdown(problem_md: str) -> list[dict[str, Any]]:
    if not problem_md:
        return []

    from sql_shell_parser import parse_shell_examples_from_markdown, parse_sql_examples_from_markdown
    from pandas_parser import parse_pandas_examples_from_markdown

    description_match = re.search(
        r"## Description\s*\n+(.*?)(?:\n## |\Z)",
        problem_md,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if description_match:
        problem_md = description_match.group(1) + "\n" + problem_md

    section_match = re.search(r"## Problem\s*\n+(.*?)(?:\n## |\Z)", problem_md, flags=re.DOTALL)
    body = section_match.group(1) if section_match else problem_md
    body = re.sub(r"^---\n.*", "", body, flags=re.DOTALL)
    body = re.sub(r"_Problem text from.*", "", body, flags=re.DOTALL)

    if re.search(r"\btable:\s*", body, flags=re.IGNORECASE):
        sql_cases = parse_sql_examples_from_markdown(problem_md)
        if sql_cases:
            return sql_cases

    if ".txt`" in body and "output" in body.lower():
        shell_cases = parse_shell_examples_from_markdown(problem_md)
        if shell_cases:
            return shell_cases

    if "dataframe" in body.lower():
        pandas_cases = parse_pandas_examples_from_markdown(problem_md)
        if pandas_cases:
            return pandas_cases

    cases: list[dict[str, Any]] = []
    for block in re.findall(r"```(?:\n|\r\n?)(.*?)```", body, flags=re.DOTALL):
        parsed = parse_example_text(block)
        if parsed:
            cases.append(parsed)

    if not cases:
        example_chunks = re.split(r"\*\*Example\s*\d*:?\s*\*\*", body, flags=re.IGNORECASE)
        for chunk in example_chunks[1:]:
            parsed = parse_example_text(chunk)
            if parsed:
                cases.append(parsed)

    if not cases:
        example_chunks = re.split(r"\*\*Example:?\*\*", body, flags=re.IGNORECASE)
        for chunk in example_chunks[1:]:
            parsed = parse_example_text(chunk)
            if parsed:
                cases.append(parsed)

    if not cases:
        cases = parse_sql_examples_from_markdown(problem_md)

    if not cases:
        cases = parse_shell_examples_from_markdown(problem_md)

    return cases
