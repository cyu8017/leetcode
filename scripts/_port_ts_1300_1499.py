#!/usr/bin/env python3
"""Port solution.js -> solution.ts for LeetCode folders 1300-1499 (skip SQL)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TREE_NODE_DEF = """class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}
"""

LIST_NODE_DEF = """class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}
"""

JSDOC_TO_TS = {
    "number": "number",
    "string": "string",
    "boolean": "boolean",
    "void": "void",
    "any": "any",
    "object": "any",
    "TreeNode": "any",
    "ListNode": "any",
    "Node": "any",
    "BinaryMatrix": "BinaryMatrix",
}


def is_sql(folder: Path) -> bool:
    cases = folder / "tests" / "cases.json"
    if not cases.exists():
        return False
    try:
        data = json.loads(cases.read_text(encoding="utf-8"))
    except Exception:
        return False
    if isinstance(data, dict):
        if data.get("kind") == "sql":
            return True
        for case in data.get("cases") or []:
            if isinstance(case, dict) and case.get("kind") == "sql":
                return True
    if isinstance(data, list):
        for case in data:
            if isinstance(case, dict) and case.get("kind") == "sql":
                return True
    return False


def is_stub(content: str) -> bool:
    if re.search(r"function\s+solve\s*\(", content):
        return True
    if re.search(r":\s*unknown\s*\{", content):
        return True
    if re.search(r"function\s+\w+\([^)]*\)\s*:\s*\w+\s*\{\s*\}", content):
        return True
    return False


def map_jsdoc_type(raw: str) -> str:
    raw = raw.strip()
    m = re.match(r"Array\.<(.+)>", raw)
    if m:
        return map_jsdoc_type(m.group(1)) + "[]"
    if raw.endswith("[]"):
        return map_jsdoc_type(raw[:-2]) + "[]"
    if raw in JSDOC_TO_TS:
        return JSDOC_TO_TS[raw]
    return "any"


def map_config_type(raw: str | None) -> str:
    if not raw:
        return "any"
    t = raw.lower().strip()
    mapping = {
        "integer": "number",
        "int": "number",
        "long": "number",
        "double": "number",
        "float": "number",
        "number": "number",
        "boolean": "boolean",
        "bool": "boolean",
        "string": "string",
        "character": "string",
        "char": "string",
        "void": "void",
        "treenode": "any",
        "listnode": "any",
        "node": "any",
        "integer[]": "number[]",
        "int[]": "number[]",
        "long[]": "number[]",
        "double[]": "number[]",
        "string[]": "string[]",
        "boolean[]": "boolean[]",
        "integer[][]": "number[][]",
        "string[][]": "string[][]",
    }
    if t in mapping:
        return mapping[t]
    if t.startswith("list<") and t.endswith(">"):
        return map_config_type(t[5:-1]) + "[]"
    if t.endswith("[]"):
        return map_config_type(t[:-2]) + "[]"
    return "any"


def parse_jsdoc_block(block: str) -> tuple[list[tuple[str | None, str]], str | None]:
    params: list[tuple[str | None, str]] = []
    ret: str | None = None
    for line in block.splitlines():
        pm = re.search(r"@param\s+\{([^}]+)\}\s+(\w+)?", line)
        if pm:
            params.append((pm.group(2), map_jsdoc_type(pm.group(1))))
            continue
        rm = re.search(r"@return(?:s)?\s+\{([^}]+)\}", line)
        if rm:
            ret = map_jsdoc_type(rm.group(1))
    return params, ret


def extract_header(js: str) -> str:
    header: list[str] = []
    for line in js.splitlines():
        stripped = line.strip()
        if stripped.startswith("//"):
            header.append(line.rstrip())
            continue
        if stripped == "":
            if header:
                header.append("")
            continue
        break
    while header and header[-1] == "":
        header.pop()
    return "\n".join(header)


def load_config_types(folder: Path) -> tuple[str | None, list[str], dict[str, str], str | None]:
    cfg_path = folder / "tests" / "config.json"
    if not cfg_path.exists():
        return None, [], {}, None
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    except Exception:
        return None, [], {}, None
    method = cfg.get("method")
    param_order = cfg.get("paramOrder") or []
    types = cfg.get("types") or {}
    class_name = cfg.get("class")
    kind = cfg.get("kind")
    if kind == "design":
        return class_name, param_order, types, "design"
    return method, param_order, types, None


def extract_balanced(text: str, open_index: int) -> str | None:
    if open_index >= len(text) or text[open_index] != "{":
        return None
    depth = 0
    in_str = None
    escape = False
    i = open_index
    while i < len(text):
        ch = text[i]
        if in_str:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == in_str:
                in_str = None
        else:
            if ch in ('"', "'", "`"):
                in_str = ch
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return text[open_index : i + 1]
        i += 1
    return None


def annotate_params(param_str: str) -> str:
    """Ensure every parameter has an explicit type (default any)."""
    if not param_str.strip():
        return ""
    parts: list[str] = []
    depth = 0
    current = []
    for ch in param_str:
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current).strip())
    typed: list[str] = []
    for part in parts:
        if not part:
            continue
        # already typed? name: type or name?: type or ...name: type
        if re.search(r":\s*[^=]+$", part.split("=")[0].strip()):
            typed.append(part)
            continue
        if "=" in part:
            name, default = part.split("=", 1)
            typed.append(f"{name.strip()}: any ={default}")
        else:
            typed.append(f"{part}: any")
    return ", ".join(typed)


def annotate_inner_functions(body: str) -> str:
    """Add : any to untyped params in nested function/arrow expressions."""

    # single-param arrow first: node =>  (avoid matching `any =>` from typed params)
    def repl_single(match: re.Match[str]) -> str:
        return f"({match.group(1)}: any) =>"

    body = re.sub(r"(?<!:)(?<![\w$])([A-Za-z_$][\w$]*)\s*=>", repl_single, body)

    def repl_arrow(match: re.Match[str]) -> str:
        params = match.group(1)
        # Already has a return type annotation: ( ... ): T =>
        if re.search(r"\)\s*:\s*[A-Za-z_$\[\]|<\s>]+$", "(" + params + ")"):
            return match.group(0)
        return f"({annotate_params(params)}): any =>"

    # (params) =>  -> (params): any =>
    body = re.sub(r"\(([^)]*)\)\s*=>", repl_arrow, body)

    # function(params) or function name(params)
    def repl_fn(match: re.Match[str]) -> str:
        return f"{match.group(1)}({annotate_params(match.group(2))})"

    body = re.sub(r"(\bfunction(?:\s+[A-Za-z_$][\w$]*)?\s*)\(([^)]*)\)", repl_fn, body)

    # empty array literals that need explicit type
    body = re.sub(r"\b(const|let)\s+(\w+)\s*=\s*\[\]", r"\1 \2: any[] = []", body)
    return body


def convert_var_function(js: str, folder: Path) -> str | None:
    method, param_order, types, kind = load_config_types(folder)
    if kind == "design":
        return None

    m = re.search(
        r"(?P<jsdoc>/\*\*.*?\*/\s*)?var\s+(?P<name>\w+)\s*=\s*function\s*\((?P<params>[^)]*)\)\s*(?P<body>\{)",
        js,
        re.S,
    )
    if not m:
        m2 = re.search(
            r"(?P<jsdoc>/\*\*.*?\*/\s*)?function\s+(?P<name>\w+)\s*\((?P<params>[^)]*)\)\s*(?P<body>\{)",
            js,
            re.S,
        )
        if not m2:
            return None
        m = m2

    name = m.group("name")
    param_str = m.group("params").strip()
    jsdoc = m.group("jsdoc") or ""
    jsdoc_params, jsdoc_ret = parse_jsdoc_block(jsdoc)
    body = extract_balanced(js, m.start("body"))
    if body is None:
        return None

    param_names = [p.strip() for p in param_str.split(",")] if param_str else []
    param_names = [re.sub(r"[=].*$", "", p).strip() for p in param_names if p]

    typed_params: list[str] = []
    for i, pname in enumerate(param_names):
        ts_type = "any"
        if i < len(jsdoc_params) and jsdoc_params[i][1]:
            ts_type = jsdoc_params[i][1]
        elif pname in types:
            ts_type = map_config_type(types.get(pname))
        elif param_order and i < len(param_order) and param_order[i] in types:
            ts_type = map_config_type(types.get(param_order[i]))
        typed_params.append(f"{pname}: {ts_type}")

    ret_type = "any"
    if jsdoc_ret:
        ret_type = jsdoc_ret
    elif "return" in types:
        ret_type = map_config_type(types.get("return"))

    fn_name = method or name
    header = extract_header(js)

    uses_new_tree = bool(re.search(r"\bnew\s+TreeNode\b", body))
    uses_new_list = bool(re.search(r"\bnew\s+ListNode\b", body))
    uses_new_node = bool(re.search(r"\bnew\s+Node\b", body))
    needs_binary_matrix = "BinaryMatrix" in js or "binaryMatrix" in param_str

    body_inner = annotate_inner_functions(body)

    parts: list[str] = []
    if header:
        parts.append(header)
        parts.append("")
    if needs_binary_matrix:
        parts.append(
            "interface BinaryMatrix {\n    get(row: number, col: number): number;\n"
            "    dimensions(): number[];\n}\n"
        )
        typed_params = [
            p.replace(": any", ": BinaryMatrix") if p.startswith("binaryMatrix:") else p
            for p in typed_params
        ]
        if ret_type == "any":
            ret_type = "number"
    if uses_new_tree:
        parts.append(TREE_NODE_DEF)
    if uses_new_list:
        parts.append(LIST_NODE_DEF)

    # Avoid DOM `Node` name collision by using a local factory.
    if uses_new_node:
        if folder.name.startswith("1490_"):
            parts.append(
                "const makeNode = (val: any, children: any = []): any => "
                "({ val, children });\n"
            )
        else:
            parts.append(
                "const makeNode = (val: any): any => "
                "({ val, left: null, right: null, random: null });\n"
            )
        body_inner = re.sub(r"\bnew\s+Node\b", "makeNode", body_inner)

    parts.append(f"function {fn_name}({', '.join(typed_params)}): {ret_type} {body_inner}")
    return "\n".join(parts).rstrip() + "\n"


def convert_design(js: str, folder: Path) -> str | None:
    class_name, _, types, kind = load_config_types(folder)
    if not class_name:
        m = re.search(r"var\s+(\w+)\s*=\s*function", js)
        if not m:
            return None
        class_name = m.group(1)

    ctor_pat = (
        r"(?P<jsdoc>/\*\*.*?\*/\s*)?var\s+"
        + re.escape(class_name)
        + r"\s*=\s*function\s*\((?P<params>[^)]*)\)\s*(?P<body>\{)"
    )
    ctor_m = re.search(ctor_pat, js, re.S)
    if not ctor_m:
        return None
    ctor_params_raw = ctor_m.group("params").strip()
    ctor_jsdoc = ctor_m.group("jsdoc") or ""
    ctor_body = extract_balanced(js, ctor_m.start("body"))
    if ctor_body is None:
        return None

    ctor_jsdoc_params, _ = parse_jsdoc_block(ctor_jsdoc)
    ctor_param_names = [p.strip() for p in ctor_params_raw.split(",")] if ctor_params_raw else []
    ctor_param_names = [re.sub(r"[=].*$", "", p).strip() for p in ctor_param_names if p]
    ctor_typed = []
    for i, pname in enumerate(ctor_param_names):
        ts_type = "any"
        if i < len(ctor_jsdoc_params):
            ts_type = ctor_jsdoc_params[i][1]
        ctor_typed.append(f"{pname}: {ts_type}")

    methods: list[tuple[str, str, str, str]] = []
    method_pat = (
        re.escape(class_name)
        + r"\.prototype\.(?P<name>\w+)\s*=\s*function\s*\((?P<params>[^)]*)\)\s*(?P<body>\{)"
    )
    for mm in re.finditer(method_pat, js, re.S):
        mname = mm.group("name")
        mparams = mm.group("params").strip()
        # Only the JSDoc immediately above this method
        before = js[: mm.start()]
        jm = re.search(r"/\*\*.*?\*/\s*$", before, re.S)
        mjsdoc = jm.group(0) if jm else ""
        mbody = extract_balanced(js, mm.start("body"))
        if mbody is None:
            continue
        jp, jr = parse_jsdoc_block(mjsdoc)
        pnames = [p.strip() for p in mparams.split(",")] if mparams else []
        pnames = [re.sub(r"[=].*$", "", p).strip() for p in pnames if p]
        typed = []
        for i, pname in enumerate(pnames):
            ts_type = "any"
            if i < len(jp):
                ts_type = jp[i][1]
            typed.append(f"{pname}: {ts_type}")
        ret = jr or "any"
        methods.append((mname, ", ".join(typed), ret, annotate_inner_functions(mbody)))

    field_names: set[str] = set()
    for body in [ctor_body] + [b for *_, b in methods]:
        for fm in re.finditer(r"this\.(\w+)\s*=", body):
            field_names.add(fm.group(1))

    header = extract_header(js)
    parts: list[str] = []
    if header:
        parts.append(header)
        parts.append("")

    parts.append(f"class {class_name} {{")
    for field in sorted(field_names):
        parts.append(f"    {field}: any;")
    ctor_sig = ", ".join(ctor_typed)
    ctor_inner = annotate_inner_functions(ctor_body[1:-1].rstrip())
    parts.append(f"    constructor({ctor_sig}) {{")
    if ctor_inner.strip():
        for line in ctor_inner.splitlines():
            parts.append(("    " + line) if line.strip() else "")
    parts.append("    }")
    for mname, typed, ret, body in methods:
        inner = body[1:-1].rstrip()
        parts.append(f"    {mname}({typed}): {ret} {{")
        if inner.strip():
            for line in inner.splitlines():
                parts.append(("    " + line) if line.strip() else "")
        parts.append("    }")
    parts.append("}")
    text = "\n".join(parts).rstrip() + "\n"
    # Fix indexed access that may be undefined (e.g. size map)
    text = re.sub(
        r"const size = (\{[^}]+\})\[(\w+)\];",
        r"const size = (\1 as Record<string, number>)[\2]!;",
        text,
    )
    return text


def convert_js_to_ts(folder: Path) -> str:
    js = (folder / "solution.js").read_text(encoding="utf-8")
    if js.startswith("\ufeff"):
        js = js[1:]

    if "prototype." in js:
        result = convert_design(js, folder)
        if result:
            return result

    result = convert_var_function(js, folder)
    if result:
        return result

    raise RuntimeError(f"Unable to convert {folder.name}")


def main() -> None:
    converted = 0
    skipped_sql = 0
    errors: list[str] = []
    for d in sorted(ROOT.iterdir()):
        if not d.is_dir():
            continue
        if not re.match(r"^1[34]\d{2}_", d.name):
            continue
        ts_path = d / "solution.ts"
        if not ts_path.exists():
            continue
        if is_sql(d):
            # Keep SQL as stub; do not overwrite if already a solve stub
            content = ts_path.read_text(encoding="utf-8") if ts_path.exists() else ""
            if not re.search(r"function\s+solve\s*\(", content):
                js = (d / "solution.js").read_text(encoding="utf-8") if (d / "solution.js").exists() else ""
                header = extract_header(js) if js else f"// LeetCode {d.name[:4]}"
                stub = (
                    (header + "\n\n" if header else "")
                    + "function solve(input: unknown): unknown {\n    return null;\n}\n"
                )
                ts_path.write_text(stub, encoding="utf-8", newline="\n")
            skipped_sql += 1
            continue
        if not (d / "solution.js").exists():
            errors.append(f"{d.name}: missing solution.js")
            continue
        try:
            ts = convert_js_to_ts(d)
            if is_stub(ts):
                errors.append(f"{d.name}: converter produced stub")
                continue
            ts_path.write_text(ts, encoding="utf-8", newline="\n")
            converted += 1
        except Exception as exc:
            errors.append(f"{d.name}: {exc}")

    print(f"converted={converted}")
    print(f"skipped_sql={skipped_sql}")
    print(f"errors={len(errors)}")
    for e in errors:
        print("ERR", e)


if __name__ == "__main__":
    main()
