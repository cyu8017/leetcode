"""Extract test runner config from LeetCode code snippets."""

from __future__ import annotations

import re
from typing import Any


TYPE_MAP = {
    "int": "integer",
    "integer": "integer",
    "float": "float",
    "double": "float",
    "bool": "boolean",
    "boolean": "boolean",
    "str": "string",
    "string": "string",
    "listnode": "listnode",
    "treenode": "treenode",
    "list[int]": "integer[]",
    "list[str]": "string[]",
    "list[string]": "string[]",
    "list[list[int]]": "integer[][]",
    "list[list[string]]": "string[][]",
}


def _normalize_type(type_hint: str) -> str | None:
    cleaned = type_hint.strip().lower().replace(" ", "")
    if cleaned in TYPE_MAP:
        return TYPE_MAP[cleaned]
    if "listnode" in cleaned:
        return "listnode"
    if "treenode" in cleaned:
        return "treenode"
    if cleaned.startswith("list[") and "list[" in cleaned[5:]:
        return "integer[][]"
    if cleaned.startswith("list["):
        return "integer[]"
    return None


def parse_python3_snippet(code: str) -> dict[str, Any] | None:
    if not code:
        return None

    class_match = re.search(
        r"class\s+(\w+)\s*:.*?def\s+(\w+)\s*\(\s*self\s*(?:,\s*([^)]*))?\)",
        code,
        flags=re.DOTALL,
    )
    if not class_match:
        return None

    class_name = class_match.group(1)
    method_name = class_match.group(2)
    params_raw = class_match.group(3) or ""

    param_order: list[str] = []
    types: dict[str, str] = {}
    for part in _split_params(params_raw):
        name, type_hint = part
        if name in {"self"}:
            continue
        param_order.append(name)
        mapped = _normalize_type(type_hint)
        if mapped in {"listnode", "treenode"}:
            types[name] = mapped

    return_match = re.search(r"->\s*([^:\n]+)", params_raw + code[class_match.end() : class_match.end() + 120])
    if return_match:
        return_type = _normalize_type(return_match.group(1))
        if return_type in {"listnode", "treenode", "integer[]", "string[]", "integer[][]"}:
            types["return"] = return_type

    return {
        "class": class_name,
        "method": method_name,
        "paramOrder": param_order,
        "types": types or None,
    }


def parse_javascript_snippet(code: str) -> dict[str, Any] | None:
    match = re.search(r"var\s+(\w+)\s*=\s*function\s*\(([^)]*)\)", code)
    if not match:
        return None
    method_name = match.group(1)
    params = [part.strip() for part in match.group(2).split(",") if part.strip()]
    return {
        "class": "Solution",
        "method": method_name,
        "paramOrder": params,
        "types": None,
    }


def parse_pandas_snippet(code: str) -> dict[str, Any] | None:
    if not code:
        return None

    match = re.search(r"def\s+(\w+)\s*\(([^)]*)\)", code)
    if not match:
        return None

    method_name = match.group(1)
    params_raw = match.group(2)
    param_order: list[str] = []
    for part in _split_params(params_raw):
        name, _type_hint = part
        if name not in {"self"}:
            param_order.append(name)

    return {
        "class": "Solution",
        "method": method_name,
        "paramOrder": param_order,
        "types": None,
    }


def parse_metadata_from_snippets(snippets: dict[str, str] | list[dict[str, str]]) -> dict[str, Any] | None:
    if isinstance(snippets, list):
        by_slug = {item.get("langSlug", ""): item.get("code", "") for item in snippets}
    else:
        by_slug = snippets

    for key in ("python3", "python", "pythondata", "java", "javascript", "typescript"):
        code = by_slug.get(key, "")
        if key == "pythondata":
            parsed = parse_pandas_snippet(code)
        elif key.startswith("python"):
            parsed = parse_python3_snippet(code)
        elif key in {"javascript", "typescript"}:
            parsed = parse_javascript_snippet(code)
        else:
            parsed = None
        if parsed:
            return parsed
    return None


def infer_param_order_from_cases(cases: list[dict[str, Any]]) -> list[str]:
    for case in cases:
        args = case.get("args")
        if isinstance(args, dict) and args:
            return list(args.keys())
    return []


def _split_params(params_raw: str) -> list[tuple[str, str]]:
    params: list[tuple[str, str]] = []
    for segment in params_raw.split(","):
        segment = segment.strip()
        if not segment:
            continue
        if ":" in segment:
            name, type_hint = segment.split(":", 1)
            params.append((name.strip(), type_hint.strip()))
        else:
            params.append((segment, ""))
    return params
