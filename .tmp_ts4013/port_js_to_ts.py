#!/usr/bin/env python3
"""Port solution.js -> solution.ts for remaining TypeScript stubs."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONTROL = {"if", "while", "for", "switch", "catch", "function", "with", "else"}

JSDOC_TYPE_MAP = {
    "number": "number",
    "string": "string",
    "boolean": "boolean",
    "null": "null",
    "undefined": "undefined",
    "void": "void",
    "any": "any",
    "object": "any",
    "Object": "any",
    "Array": "any[]",
    "integer": "number",
    "int": "number",
    "long": "number",
    "double": "number",
    "float": "number",
    "character": "string",
    "char": "string",
    "TreeNode": "TreeNode | null",
    "ListNode": "ListNode | null",
    "Node": "Node | null",
    "narynode": "Node | null",
    "NaryNode": "Node | null",
}


def is_ts_stub(text: str) -> bool:
    t = text.strip()
    if re.search(
        r"function\s+solve\s*\(\s*input\s*:\s*unknown\s*\)\s*:\s*unknown\s*\{\s*return\s+null;\s*\}",
        t,
    ):
        return True
    if re.search(r"function\s+solve\s*\([^)]*\)\s*:\s*unknown\s*\{\s*return\s+null", t) and t.count(
        "function "
    ) <= 1:
        return True
    return False


def find_matching_brace(text: str, open_idx: int) -> int:
    depth = 0
    in_str = None
    escape = False
    j = open_idx
    while j < len(text):
        ch = text[j]
        if in_str:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == in_str:
                in_str = None
        else:
            if ch in ("'", '"', "`"):
                in_str = ch
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return j
        j += 1
    return -1


def map_jsdoc_type(raw: str | None) -> str:
    if not raw:
        return "any"
    raw = raw.strip().strip("{}").strip()
    if not raw:
        return "any"
    if "|" in raw:
        parts = []
        for p in raw.split("|"):
            mapped = map_jsdoc_type(p.strip())
            if mapped not in parts:
                parts.append(mapped)
        return " | ".join(parts)
    m = re.match(r"Array\.<(.+)>", raw)
    if m:
        return f"{map_jsdoc_type(m.group(1))}[]"
    if raw.endswith("[]"):
        inner = map_jsdoc_type(raw[:-2])
        if inner.endswith(" | null") and inner[:-8] in {"TreeNode", "ListNode", "Node"}:
            # TreeNode[] should stay TreeNode[]
            inner = inner[:-8]
        return f"{inner}[]"
    if raw in JSDOC_TYPE_MAP:
        return JSDOC_TYPE_MAP[raw]
    if re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", raw):
        return raw
    return "any"


def parse_jsdoc_block(block: str) -> tuple[list[tuple[str, str]], str | None]:
    params: list[tuple[str, str]] = []
    ret: str | None = None
    for line in block.splitlines():
        line = line.strip().lstrip("*").strip()
        pm = re.match(r"@param\s+\{([^}]+)\}\s+(\w+)", line)
        if pm:
            params.append((pm.group(2), map_jsdoc_type(pm.group(1))))
            continue
        rm = re.match(r"@return(?:s)?\s+\{([^}]+)\}", line)
        if rm:
            ret = map_jsdoc_type(rm.group(1))
    return params, ret


def type_params(params_raw: str, param_types: dict[str, str]) -> str:
    typed = []
    if not params_raw.strip():
        return ""
    # split params ignoring nested parens/brackets
    parts: list[str] = []
    buf = []
    depth = 0
    for ch in params_raw:
        if ch in "([{":
            depth += 1
            buf.append(ch)
        elif ch in ")]}":
            depth -= 1
            buf.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    if buf:
        parts.append("".join(buf).strip())
    for p in parts:
        if not p:
            continue
        if p.startswith("..."):
            name = p[3:].strip()
            ptype = param_types.get(name, "any[]")
            typed.append(f"...{name}: {ptype}")
            continue
        if "=" in p:
            pname, default = [x.strip() for x in p.split("=", 1)]
            ptype = param_types.get(pname, "any")
            typed.append(f"{pname}: {ptype} = {default}")
        else:
            ptype = param_types.get(p, "any")
            typed.append(f"{p}: {ptype}")
    return ", ".join(typed)


def extract_header(js: str) -> tuple[str, str]:
    js = js.lstrip("\ufeff")
    m = re.match(r"((?://[^\n]*\n)+)\s*\n?", js)
    if not m:
        return "", js
    header = m.group(1)
    if not header.endswith("\n"):
        header += "\n"
    if not header.endswith("\n\n"):
        header += "\n"
    return header, js[m.end() :]


def extract_query(js: str) -> str | None:
    m = re.search(r"(?:export\s+)?(?:const|var|let)\s+QUERY\s*=\s*`([^`]*)`", js, re.S)
    if m:
        return m.group(1).strip()
    m = re.search(r"QUERY\s*=\s*(\"\"\"|''' )(.*?)\1", js, re.S)
    return None


def preceding_jsdoc(text: str, idx: int) -> str:
    before = text[:idx].rstrip()
    if before.endswith("*/"):
        start = before.rfind("/**")
        if start >= 0:
            return text[start:idx]
    return ""


def convert_var_functions(js: str) -> str:
    result: list[str] = []
    i = 0
    pattern = re.compile(
        r"(?P<jsdoc>/\*\*[\s\S]*?\*/\s*)?(?:export\s+)?var\s+(?P<name>\w+)\s*=\s*(?P<async>async\s+)?function\s*\((?P<params>[^)]*)\)\s*\{"
    )
    while True:
        m = pattern.search(js, i)
        if not m:
            result.append(js[i:])
            break
        result.append(js[i : m.start()])
        name = m.group("name")
        params_raw = m.group("params")
        jd = m.group("jsdoc")
        async_kw = "async " if m.group("async") else ""

        param_types: dict[str, str] = {}
        ret_type = "any"
        if jd:
            plist, ret = parse_jsdoc_block(jd)
            param_types = {n: t for n, t in plist}
            if ret:
                ret_type = ret

        body_start = m.end() - 1
        body_end = find_matching_brace(js, body_start)
        if body_end < 0:
            result.append(js[m.start() :])
            break
        body = js[body_start + 1 : body_end]
        k = body_end + 1
        while k < len(js) and js[k] in " \t\r":
            k += 1
        if k < len(js) and js[k] == ";":
            k += 1
        while k < len(js) and js[k] in " \t\r":
            k += 1
        if k < len(js) and js[k] == "\n":
            k += 1

        params = type_params(params_raw, param_types)
        result.append(f"export {async_kw}function {name}({params}): {ret_type} {{{body}}}")
        i = k
    return "".join(result)


def convert_bare_functions(js: str) -> str:
    """Type leftover `function name(params) {` helpers (not constructors with this.)."""
    result: list[str] = []
    i = 0
    pattern = re.compile(
        r"(?P<jsdoc>/\*\*[\s\S]*?\*/\s*)?(?P<async>async\s+)?function\s+(?P<name>\w+)\s*\((?P<params>[^)]*)\)\s*\{"
    )
    while True:
        m = pattern.search(js, i)
        if not m:
            result.append(js[i:])
            break
        name = m.group("name")
        # skip if already converted/exported with types in the match prefix... still convert
        result.append(js[i : m.start()])
        jd = m.group("jsdoc") or ""
        async_kw = "async " if m.group("async") else ""
        params_raw = m.group("params")
        param_types: dict[str, str] = {}
        ret_type = "any"
        if jd:
            plist, ret = parse_jsdoc_block(jd)
            param_types = {n: t for n, t in plist}
            if ret:
                ret_type = ret
        body_start = m.end() - 1
        body_end = find_matching_brace(js, body_start)
        if body_end < 0:
            result.append(js[m.start() :])
            break
        body = js[body_start + 1 : body_end]
        # constructor-style helper: keep as class later; here type it loosely
        params = type_params(params_raw, param_types)
        export = "export " if name[0].isupper() is False else ""
        # helpers like lowerBound stay unexported; main leetcode fns already converted as export
        result.append(f"{async_kw}function {name}({params}): {ret_type} {{{body}}}")
        i = body_end + 1
        if i < len(js) and js[i] == "\n":
            i += 1
    return "".join(result)


def convert_prototype_class(js: str, class_name: str) -> str | None:
    """Convert `var Name = function` + `Name.prototype.x = function` into export class."""
    ctor_pat = re.compile(
        rf"(?P<jsdoc>/\*\*[\s\S]*?\*/\s*)?var\s+{re.escape(class_name)}\s*=\s*function\s*\((?P<params>[^)]*)\)\s*\{{"
    )
    m = ctor_pat.search(js)
    if not m:
        fn_pat = re.compile(
            rf"(?P<jsdoc>/\*\*[\s\S]*?\*/\s*)?function\s+{re.escape(class_name)}\s*\((?P<params>[^)]*)\)\s*\{{"
        )
        m = fn_pat.search(js)
        if not m:
            return None
    jd = m.group("jsdoc") or preceding_jsdoc(js, m.start())
    plist, _ = parse_jsdoc_block(jd) if jd else ([], None)
    param_types = {n: t for n, t in plist}
    params = type_params(m.group("params"), param_types)
    body_start = m.end() - 1
    body_end = find_matching_brace(js, body_start)
    ctor_body = js[body_start + 1 : body_end]
    used = [(m.start(), body_end + 1)]

    methods: list[str] = []
    proto_pat = re.compile(
        rf"(?P<jsdoc>/\*\*[\s\S]*?\*/\s*)?{re.escape(class_name)}\.prototype\.(?P<name>\w+)\s*=\s*(?P<async>async\s+)?function\s*\((?P<params>[^)]*)\)\s*\{{"
    )
    for pm in proto_pat.finditer(js):
        pjd = pm.group("jsdoc") or ""
        pplist, pret = parse_jsdoc_block(pjd) if pjd else ([], None)
        ptypes = {n: t for n, t in pplist}
        pparams = type_params(pm.group("params"), ptypes)
        rtype = pret or "any"
        async_kw = "async " if pm.group("async") else ""
        pb_start = pm.end() - 1
        pb_end = find_matching_brace(js, pb_start)
        pbody = js[pb_start + 1 : pb_end]
        methods.append(f"    {async_kw}{pm.group('name')}({pparams}): {rtype} {{{pbody}}}")
        used.append((pm.start(), pb_end + 1))

    if not methods and "this." not in ctor_body:
        return None

    # strip consumed pieces from remaining js later by caller
    class_src = f"export class {class_name} {{\n    constructor({params}) {{{ctor_body}}}\n" + (
        "\n".join(methods) + "\n" if methods else ""
    ) + "}\n"
    return class_src, used


def convert_host_prototype(js: str) -> str:
    """Host.prototype.foo = function(...) { this } -> export function foo(host, ...)."""
    pattern = re.compile(
        r"(?P<jsdoc>/\*\*[\s\S]*?\*/\s*)?(?P<host>Array|Function|Date|String|Object|Promise)\.prototype\.(?P<name>\w+)\s*=\s*(?P<async>async\s+)?function\s*\((?P<params>[^)]*)\)\s*\{"
    )
    result: list[str] = []
    i = 0
    while True:
        m = pattern.search(js, i)
        if not m:
            result.append(js[i:])
            break
        result.append(js[i : m.start()])
        name = m.group("name")
        async_kw = "async " if m.group("async") else ""
        params_raw = m.group("params")
        jd = m.group("jsdoc") or ""
        plist, pret = parse_jsdoc_block(jd) if jd else ([], None)
        ptypes = {n: t for n, t in plist}
        extra = type_params(params_raw, ptypes)
        rtype = pret or "any"
        body_start = m.end() - 1
        body_end = find_matching_brace(js, body_start)
        body = js[body_start + 1 : body_end]
        host = m.group("host")
        host_type = {
            "Array": "any[]",
            "Function": "Function",
            "Date": "Date",
            "String": "string",
            "Object": "any",
            "Promise": "Promise<any>",
        }[host]
        body = re.sub(r"\bthis\b", "self", body)
        params = f"self: {host_type}" + (f", {extra}" if extra else "")
        result.append(f"export {async_kw}function {name}({params}): {rtype} {{{body}}}")
        k = body_end + 1
        if k < len(js) and js[k] == ";":
            k += 1
        i = k
    return "".join(result)


def convert_js_class(js: str) -> str:
    js = re.sub(r"(?m)^class\s+(\w+)", r"export class \1", js)
    # type methods without types
    m = re.search(r"export class\s+(\w+)\s*\{", js)
    if not m:
        return js
    open_idx = m.end() - 1
    close_idx = find_matching_brace(js, open_idx)
    if close_idx < 0:
        return js
    before = js[: open_idx + 1]
    after = js[close_idx:]
    body = js[open_idx + 1 : close_idx]
    method_re = re.compile(r"(constructor|[A-Za-z_]\w*)\s*\(([^)]*)\)\s*\{")
    out: list[str] = []
    i = 0
    depth = 0
    in_str = None
    escape = False
    while i < len(body):
        if depth == 0 and in_str is None:
            m2 = method_re.match(body, i)
            if m2 and m2.group(1) not in CONTROL:
                name = m2.group(1)
                params_raw = m2.group(2)
                # skip if already typed (contains :)
                if ":" not in params_raw.split("=")[0] if False else (":" not in m2.group(0).split("{")[0]):
                    params = type_params(params_raw, {})
                    brace_idx = m2.end() - 1
                    end = find_matching_brace(body, brace_idx)
                    method_body = body[brace_idx + 1 : end]
                    if name == "constructor":
                        out.append(f"constructor({params}) {{{method_body}}}")
                    else:
                        out.append(f"{name}({params}): any {{{method_body}}}")
                    i = end + 1
                    continue
        ch = body[i]
        if in_str:
            out.append(ch)
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == in_str:
                in_str = None
            i += 1
            continue
        if ch in ("'", '"', "`"):
            in_str = ch
            out.append(ch)
            i += 1
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        out.append(ch)
        i += 1
    return before + "".join(out) + after


TREE_NODE = """class TreeNode {
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

LIST_NODE = """class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

"""

NARY_NODE = """class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

"""

QUAD_NODE = """class Node {
    val: boolean;
    isLeaf: boolean;
    topLeft: Node | null;
    topRight: Node | null;
    bottomLeft: Node | null;
    bottomRight: Node | null;
    constructor(val?: boolean, isLeaf?: boolean, topLeft?: Node | null, topRight?: Node | null, bottomLeft?: Node | null, bottomRight?: Node | null) {
        this.val = val ?? false;
        this.isLeaf = isLeaf ?? false;
        this.topLeft = topLeft ?? null;
        this.topRight = topRight ?? null;
        this.bottomLeft = bottomLeft ?? null;
        this.bottomRight = bottomRight ?? null;
    }
}

"""

RANDOM_NODE = """class Node {
    val: number;
    next: Node | null;
    random: Node | null;
    constructor(val?: number, next?: Node | null, random?: Node | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
        this.random = random ?? null;
    }
}

"""


def add_node_types(ts: str, folder_name: str) -> str:
    extras = []
    if re.search(r"\bTreeNode\b", ts) and "class TreeNode" not in ts:
        extras.append(TREE_NODE)
    if re.search(r"\bListNode\b", ts) and "class ListNode" not in ts:
        extras.append(LIST_NODE)
    if re.search(r"\bNode\b", ts) and "class Node" not in ts and "interface Node" not in ts:
        if "topLeft" in ts or "isLeaf" in ts:
            extras.append(QUAD_NODE)
        elif "random" in ts:
            extras.append(RANDOM_NODE)
        elif "children" in ts:
            extras.append(NARY_NODE)
        else:
            extras.append(NARY_NODE)
    if not extras:
        return ts
    m = re.match(r"((?://[^\n]*\n)+\n*)", ts)
    if m:
        return m.group(1) + "".join(extras) + ts[m.end() :]
    return "".join(extras) + ts


def strip_jsdoc(ts: str) -> str:
    ts = re.sub(r"/\*\*[\s\S]*?\*/\s*", "", ts)
    ts = re.sub(r"\n?module\.exports\s*=\s*\{[^}]*\}\s*;?\s*", "\n", ts)
    ts = re.sub(r"\n{3,}", "\n\n", ts)
    return ts


def convert_js_to_ts(js: str, folder_name: str) -> str:
    js = js.lstrip("\ufeff").replace("\r\n", "\n")
    header, body = extract_header(js)

    query = extract_query(js)
    if query is not None and not re.search(r"var\s+\w+\s*=\s*(async\s+)?function", body.replace("QUERY", "", 1) if False else body):
        # SQL-only if QUERY is the main export and no real functions besides maybe none
        if not re.search(r"var\s+(?!QUERY)\w+\s*=\s*(async\s+)?function", body) and not re.search(
            r"(?m)^function\s+\w+", body
        ) and not re.search(r"(?m)^class\s+\w+", body):
            return header + f"export const QUERY = `{query}`;\n"

    if re.search(r"(Array|Function|Date|String|Object|Promise)\.prototype\.", body):
        body = convert_host_prototype(body)

    # Prototype classes / constructor functions
    proto_names = set(re.findall(r"(\w+)\.prototype\.\w+", body))
    ctor_names = set(re.findall(r"var\s+(\w+)\s*=\s*function\s*\(", body))
    fn_ctor_names = set()
    for n in proto_names:
        if re.search(rf"function\s+{n}\s*\(", body):
            fn_ctor_names.add(n)

    class_chunks: list[str] = []
    used_spans: list[tuple[int, int]] = []
    for name in sorted(proto_names | (ctor_names & proto_names) | fn_ctor_names):
        converted = convert_prototype_class(body, name)
        if not converted:
            continue
        src, spans = converted
        class_chunks.append(src)
        used_spans.extend(spans)

    if used_spans:
        keep = []
        last = 0
        for a, b in sorted(used_spans):
            if a > last:
                keep.append(body[last:a])
            last = max(last, b)
            # skip trailing semicolon
            if last < len(body) and body[last] == ";":
                last += 1
        keep.append(body[last:])
        body = "".join(keep)
        body = "\n".join(class_chunks) + "\n" + body

    if re.search(r"(?m)^class\s+\w+", body) or re.search(r"(?m)^export class\s+\w+", body):
        body = convert_js_class(body)

    if re.search(r"var\s+\w+\s*=\s*(async\s+)?function", body):
        body = convert_var_functions(body)

    if re.search(r"(?:async\s+)?function\s+\w+\s*\(", body):
        body = convert_bare_functions(body)

    body = strip_jsdoc(body).strip() + "\n"
    ts = header + body
    ts = add_node_types(ts, folder_name)
    ts = ts.replace("tree: Node | null[]", "tree: Node[]")
    return ts


def fill_sql(folder: Path) -> bool:
    cfg = folder / "tests" / "config.json"
    kind = "algo"
    if cfg.exists():
        try:
            kind = json.loads(cfg.read_text()).get("kind") or "algo"
        except Exception:
            pass
    js = (folder / "solution.js").read_text(encoding="utf-8-sig", errors="replace")
    py = folder / "solution.py"
    query = None
    m = re.search(r"(?:export\s+)?(?:const|var|let)\s+QUERY\s*=\s*`([^`]*)`", js, re.S)
    if m:
        query = m.group(1).strip()
    elif py.exists():
        pm = re.search(r'QUERY\s*=\s*("""|\'\'\')(.*?)\1', py.read_text(encoding="utf-8-sig", errors="replace"), re.S)
        if pm:
            query = pm.group(2).strip()
    if kind != "sql" and query is None:
        return False
    if not query:
        return False
    num = folder.name.split("_")[0]
    title = folder.name[5:].replace("_", " ").title()
    slug = folder.name[5:].replace("_", "-")
    text = (
        f"// LeetCode {num} - {title}\n"
        f"// https://leetcode.com/problems/{slug}/\n\n"
        f"export const QUERY = `{query}`;\n"
    )
    (folder / "solution.ts").write_text(text, encoding="utf-8")
    return True


def main() -> None:
    stubs_path = Path(__file__).parent / "stubs.txt"
    stubs = stubs_path.read_text().splitlines()
    sql_n = port_n = fail = 0
    failed: list[str] = []
    for name in stubs:
        folder = ROOT / name
        ts_path = folder / "solution.ts"
        if ts_path.exists() and not is_ts_stub(ts_path.read_text(encoding="utf-8-sig", errors="replace")):
            continue
        try:
            if fill_sql(folder):
                # only count as sql if config says sql OR js is query-only
                cfg = folder / "tests" / "config.json"
                kind = "algo"
                if cfg.exists():
                    try:
                        kind = json.loads(cfg.read_text()).get("kind") or "algo"
                    except Exception:
                        pass
                js = (folder / "solution.js").read_text(encoding="utf-8-sig", errors="replace")
                query_only = bool(re.search(r"(?:var|const|let)\s+QUERY\s*=", js)) and not re.search(
                    r"var\s+(?!QUERY)\w+\s*=\s*(async\s+)?function", js
                )
                if kind == "sql" or query_only:
                    sql_n += 1
                    continue
            js = (folder / "solution.js").read_text(encoding="utf-8-sig", errors="replace")
            ts = convert_js_to_ts(js, name)
            if is_ts_stub(ts) or not ts.strip():
                failed.append(name)
                fail += 1
                continue
            ts_path.write_text(ts, encoding="utf-8")
            port_n += 1
        except Exception as e:
            failed.append(f"{name}: {e}")
            fail += 1
    print(f"sql={sql_n} ported={port_n} failed={fail}")
    for x in failed[:40]:
        print(" FAIL", x)


if __name__ == "__main__":
    main()
