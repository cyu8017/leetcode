"""Build tests/config.json from LeetCode metadata and parsed cases."""

from __future__ import annotations

from typing import Any

from metadata_parser import infer_param_order_from_cases, parse_metadata_from_snippets


def infer_types_from_cases(cases: list[dict[str, Any]]) -> dict[str, str] | None:
    types: dict[str, str] = {}
    for case in cases:
        args = case.get("args")
        if not isinstance(args, dict):
            continue
        for key in args:
            if key in {"head", "l1", "l2"}:
                types[key] = "listnode"
            elif key == "root":
                types[key] = "treenode"
    return types or None


def build_config(existing: dict[str, Any], metadata: dict[str, Any] | None, cases: list[dict[str, Any]]) -> dict[str, Any]:
    config = dict(existing)

    if cases and cases[0].get("kind") == "design":
        config["kind"] = "design"
        config["class"] = cases[0]["operations"][0]
        config.pop("method", None)
        config.pop("paramOrder", None)
        config.pop("types", None)
        config["runnable"] = True
        return config

    if cases and cases[0].get("kind") == "sql":
        config["kind"] = "sql"
        config["class"] = config.get("class", "Solution")
        config["method"] = "query"
        config["runnable"] = False
        config.pop("paramOrder", None)
        config.pop("types", None)
        return config

    if cases and cases[0].get("kind") == "shell":
        config["kind"] = "shell"
        config["class"] = config.get("class", "Solution")
        config["method"] = "run"
        config["file"] = cases[0].get("file", "input.txt")
        config["runnable"] = False
        return config

    if cases and cases[0].get("kind") == "pandas":
        config["kind"] = "pandas"
        config["class"] = "Solution"
        config["method"] = metadata.get("method", config.get("method", "solve")) if metadata else config.get("method", "solve")
        if metadata and metadata.get("paramOrder"):
            config["paramOrder"] = metadata["paramOrder"]
        elif not config.get("paramOrder"):
            inferred = infer_param_order_from_cases(cases)
            if inferred:
                config["paramOrder"] = inferred
        config["runnable"] = False
        config.pop("types", None)
        return config

    config.pop("kind", None)
    config.pop("runnable", None)

    if metadata:
        config["class"] = metadata.get("class", config.get("class", "Solution"))
        config["method"] = metadata.get("method", config.get("method", "solve"))
        if metadata.get("paramOrder"):
            config["paramOrder"] = metadata["paramOrder"]
        if metadata.get("types"):
            config["types"] = metadata["types"]
    elif not config.get("paramOrder"):
        inferred = infer_param_order_from_cases(cases)
        if inferred:
            config["paramOrder"] = inferred

    inferred_types = infer_types_from_cases(cases)
    if inferred_types and not config.get("types"):
        config["types"] = inferred_types

    if config.get("method") == "solve" and metadata and metadata.get("method"):
        config["method"] = metadata["method"]

    return config


def metadata_from_neenza(neenza_entry: dict[str, Any] | None) -> dict[str, Any] | None:
    if not neenza_entry:
        return None
    snippets = neenza_entry.get("code_snippets") or []
    return parse_metadata_from_snippets(snippets)
