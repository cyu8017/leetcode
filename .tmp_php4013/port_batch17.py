#!/usr/bin/env python3
"""Convert batch_17 JS solutions to PHP and write solution.php files."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
BATCH = (ROOT / ".tmp_php4013/batch_17.txt").read_text().strip().splitlines()

KEYWORDS = {
    "true", "false", "null", "return", "if", "else", "for", "while", "break",
    "continue", "function", "class", "new", "this", "instanceof", "typeof",
    "void", "in", "of", "case", "default", "switch", "try", "catch", "finally",
    "throw", "const", "let", "var", "static", "public", "private", "protected",
    "use", "as", "echo", "array", "unset", "isset", "empty", "list",
}

PHP_BUILTINS = {
    "count", "strlen", "substr", "strpos", "ord", "chr", "intval", "intdiv",
    "max", "min", "abs", "floor", "ceil", "array_fill", "array_slice",
    "array_pop", "array_shift", "array_push", "array_values", "array_keys",
    "array_key_exists", "array_merge", "array_reverse", "array_unique",
    "sort", "rsort", "usort", "ksort", "implode", "explode", "str_split",
    "isset", "unset", "empty", "intval", "floatval", "strval", "sprintf",
    "strcmp", "strnatcmp", "PHP_INT_MAX", "PHP_INT_MIN", "INF",
    "array_flip", "in_array", "end", "reset", "key", "current", "next",
    "preg_match", "preg_split", "join", "range", "intval",
}

STRING_HINTS = {
    "s", "t", "word", "p", "caption", "text", "formula", "cell",
    "str1", "str2", "left", "right", "cand", "msg", "part", "pattern",
    "w", "c", "ch", "numbers", "a0", "b0",
}

SKIP_METHODS = {
    "length", "push", "pop", "shift", "unshift", "slice", "sort", "map",
    "filter", "reduce", "forEach", "indexOf", "includes", "substring",
    "substr", "charCodeAt", "charAt", "split", "join", "reverse", "fill",
    "has", "get", "set", "delete", "add", "values", "keys", "entries",
    "localeCompare", "toString", "concat", "startsWith", "endsWith",
}


def title_from_folder(folder: str) -> tuple[int, str]:
    num = int(folder.split("_")[0])
    words = folder.split("_")[1:]
    pretty = []
    small = {"of", "to", "in", "a", "an", "the", "and", "or", "for", "with", "by", "from", "after", "on"}
    for i, w in enumerate(words):
        if i > 0 and w in small:
            pretty.append(w)
        else:
            pretty.append(w.capitalize() if w not in {"i", "ii", "iii", "iv", "k"} else w.upper())
    # Prefer header from JS
    return num, " ".join(pretty)


def js_header(js: str) -> tuple[str, str]:
    lines = js.splitlines()
    title = ""
    url = ""
    for line in lines[:6]:
        if line.startswith("// LeetCode"):
            title = line
        if "leetcode.com/problems" in line:
            url = line
    return title, url


def strip_jsdoc(s: str) -> str:
    return re.sub(r"/\*\*.*?\*/", "", s, flags=re.S)


def extract_main(js: str) -> tuple[str, list[str], str] | None:
    """Return (name, args, body) for `var name = function(args) { body }`."""
    m = re.search(
        r"var\s+(\w+)\s*=\s*function\s*\(([^)]*)\)\s*\{",
        js,
    )
    if not m:
        return None
    name = m.group(1)
    args = [a.strip() for a in m.group(2).split(",") if a.strip()]
    start = m.end()
    # find matching close of function
    depth = 1
    i = start
    while i < len(js):
        if js[i] == "{":
            depth += 1
        elif js[i] == "}":
            depth -= 1
            if depth == 0:
                return name, args, js[start:i]
        i += 1
    return name, args, js[start:]


def extract_class(js: str) -> tuple[str, str] | None:
    m = re.search(r"class\s+(\w+)\s*\{", js)
    if not m:
        return None
    name = m.group(1)
    start = m.end()
    depth = 1
    i = start
    while i < len(js):
        if js[i] == "{":
            depth += 1
        elif js[i] == "}":
            depth -= 1
            if depth == 0:
                return name, js[start:i]
        i += 1
    return name, js[start:]


def find_nested_fns(body: str) -> list[tuple[str, list[str], str, int, int]]:
    """Find const/let name = (args) => { } or function(args) { } at top-ish level."""
    results = []
    patterns = [
        re.compile(r"\b(?:const|let|var)\s+(\w+)\s*=\s*\(([^)]*)\)\s*=>\s*\{"),
        re.compile(r"\b(?:const|let|var)\s+(\w+)\s*=\s*function\s*\(([^)]*)\)\s*\{"),
    ]
    for pat in patterns:
        for m in pat.finditer(body):
            name = m.group(1)
            args = [a.strip() for a in m.group(2).split(",") if a.strip()]
            start = m.end()
            depth = 1
            i = start
            while i < len(body):
                if body[i] == "{":
                    depth += 1
                elif body[i] == "}":
                    depth -= 1
                    if depth == 0:
                        results.append((name, args, body[start:i], m.start(), i + 1))
                        break
                i += 1
    # also one-liners: const gcd = (a, b) => { ... } already handled
    # const gcd = (a, b) => expr;
    pat2 = re.compile(
        r"\b(?:const|let|var)\s+(\w+)\s*=\s*\(([^)]*)\)\s*=>\s*(?=\{)?"
    )
    return sorted(results, key=lambda x: x[3])


def collect_outer_vars(body: str, params: list[str], nested_names: list[str]) -> list[str]:
    names = set(params) | set(nested_names)
    for m in re.finditer(r"\b(?:const|let|var)\s+([A-Za-z_]\w*)", body):
        names.add(m.group(1))
    # multi-decl: let a = 0, b = 1
    for m in re.finditer(r"\b(?:const|let|var)\s+([^;]+);", body):
        chunk = m.group(1)
        for part in chunk.split(","):
            mm = re.match(r"\s*([A-Za-z_]\w*)", part.strip())
            if mm:
                names.add(mm.group(1))
    return sorted(names)


def dollarize_expr(expr: str, string_vars: set[str]) -> str:
    """Convert a JS expression/statement block to PHP-ish syntax."""
    s = expr

    # comments stay

    # BigInt / Number wrappers
    s = re.sub(r"\bNumber\s*\(([^)]+)\)", r"(\1)", s)
    s = re.sub(r"\bBigInt\s*\(([^)]+)\)", r"(\1)", s)
    s = re.sub(r"\b(\d+)n\b", r"\1", s)

    # Infinity / Number extremes
    s = s.replace("Number.MIN_SAFE_INTEGER", "PHP_INT_MIN")
    s = s.replace("Number.MAX_SAFE_INTEGER", "PHP_INT_MAX")
    s = re.sub(r"(?<![\w$])Infinity\b", "INF", s)

    # parseInt
    s = re.sub(r"parseInt\s*\(([^,]+),\s*10\s*\)", r"intval(\1)", s)
    s = re.sub(r"parseInt\s*\(([^)]+)\)", r"intval(\1)", s)

    # Math
    s = re.sub(r"Math\.floor\s*\(\s*\(([^)]+)\)\s*/\s*2\s*\)", r"intdiv((\1), 2)", s)
    s = re.sub(r"Math\.floor\s*\(\s*([^/]+?)\s*/\s*2\s*\)", r"intdiv(\1, 2)", s)
    s = re.sub(r"Math\.floor\s*\(([^)]+)\)", r"intval(floor(\1))", s)
    s = re.sub(r"Math\.ceil\s*\(([^)]+)\)", r"intval(ceil(\1))", s)
    s = s.replace("Math.max", "max")
    s = s.replace("Math.min", "min")
    s = s.replace("Math.abs", "abs")

    # Array.from({ length: n }, () => new Array(m).fill(v))
    s = re.sub(
        r"Array\.from\(\s*\{\s*length:\s*([^}]+)\}\s*,\s*\(\)\s*=>\s*new Array\(([^)]+)\)\.fill\(([^)]+)\)\s*\)",
        r"(function($__n, $__m, $__v) { $__a = []; for ($__i = 0; $__i < ($__n); $__i++) $__a[] = array_fill(0, $__m, $__v); return $__a; })(\1, \2, \3)",
        s,
    )
    s = re.sub(
        r"Array\.from\(\s*\{\s*length:\s*([^}]+)\}\s*,\s*\(\)\s*=>\s*new Array\((\d+)\)\.fill\(([^)]+)\)\s*\)",
        r"(function($__n) { $__a = []; for ($__i = 0; $__i < ($__n); $__i++) $__a[] = array_fill(0, \2, \3); return $__a; })(\1)",
        s,
    )
    s = re.sub(
        r"Array\.from\(\s*\{\s*length:\s*([^}]+)\}\s*,\s*\(\)\s*=>\s*\[\s*\]\s*\)",
        r"array_fill(0, \1, [])",
        s,
    )
    s = re.sub(
        r"Array\.from\(\s*\{\s*length:\s*([^}]+)\}\s*,\s*\(\)\s*=>\s*0\s*\)",
        r"array_fill(0, \1, 0)",
        s,
    )

    # new Array(n).fill(x)
    s = re.sub(r"new Array\(([^)]+)\)\.fill\(([^)]+)\)", r"array_fill(0, \1, \2)", s)
    s = re.sub(r"new Array\(([^)]+)\)", r"array_fill(0, \1, null)", s)

    # new Map / Set
    s = re.sub(r"new Map\(\s*\)", "[]", s)
    s = re.sub(r"new Set\(\s*\)", "[]", s)
    s = re.sub(r"new Set\(([^)]+)\)", r"array_fill_keys(\1, true)", s)

    # slice().sort
    # handle later after methods

    # object literals { a: b, c: d } — simple one-level
    def repl_obj(m):
        inner = m.group(1)
        if "function" in inner or "=>" in inner:
            return m.group(0)
        parts = []
        # split on commas not inside []
        buf = ""
        depth = 0
        for ch in inner + ",":
            if ch in "[{(":
                depth += 1
                buf += ch
            elif ch in "]})":
                depth -= 1
                buf += ch
            elif ch == "," and depth == 0:
                part = buf.strip()
                buf = ""
                if not part:
                    continue
                if ":" in part:
                    k, v = part.split(":", 1)
                    k = k.strip()
                    if re.match(r"^[\w]+$", k):
                        parts.append(f"'{k}' => {v.strip()}")
                    else:
                        return m.group(0)
                else:
                    # shorthand { i }
                    k = part
                    if re.match(r"^[\w]+$", k):
                        parts.append(f"'{k}' => {k}")
                    else:
                        return m.group(0)
            else:
                buf += ch
        return "[" + ", ".join(parts) + "]"

    s = re.sub(r"\{\s*([^{}]+)\s*\}", repl_obj, s)

    return s


def convert_methods(s: str, string_vars: set[str]) -> str:
    # this.foo
    s = re.sub(r"\bthis\.(\w+)", r"$this->\1", s)

    # Map/Set ops — do before generic property
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.delete\(([^)]+)\)", r"unset(\1[\2])", s)
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.set\(([^,]+),\s*([^)]+)\)", r"\1[\2] = \3", s)
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.get\(([^)]+)\)", r"(\1[\2] ?? null)", s)
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.has\(([^)]+)\)", r"isset(\1[\2])", s)
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.add\(([^)]+)\)", r"\1[\2] = true", s)
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.values\(\)", r"\1", s)

    # charCodeAt
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.charCodeAt\((\d+)\)", r"ord(\1[\2])", s)
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.charCodeAt\(([^)]+)\)", r"ord(\1[\2])", s)

    # substring
    def repl_sub(m):
        obj, args = m.group(1), m.group(2)
        parts = [p.strip() for p in args.split(",")]
        if len(parts) == 1:
            return f"substr({obj}, {parts[0]})"
        return f"substr({obj}, {parts[0]}, ({parts[1]}) - ({parts[0]}))"

    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.substring\(([^)]*)\)", repl_sub, s)

    # indexOf
    def repl_idx(m):
        obj, args = m.group(1), m.group(2)
        parts = [p.strip() for p in args.split(",")]
        if len(parts) == 1:
            return f"strpos({obj}, {parts[0]})"
        return f"strpos({obj}, {parts[0]}, {parts[1]})"

    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.indexOf\(([^)]*)\)", repl_idx, s)

    # split / join
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.split\(([^)]+)\)", r"explode(\2, \1)", s)
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.join\(([^)]+)\)", r"implode(\2, \1)", s)

    # push / pop / shift
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.push\(([^)]+)\)", r"\1[] = \2", s)
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.pop\(\)", r"array_pop(\1)", s)
    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.shift\(\)", r"array_shift(\1)", s)

    # slice
    def repl_slice(m):
        obj, args = m.group(1), m.group(2)
        parts = [p.strip() for p in args.split(",") if p.strip()]
        if not parts:
            return f"{obj}"  # copy; PHP arrays copy on assign
        if len(parts) == 1:
            return f"array_slice({obj}, {parts[0]})"
        return f"array_slice({obj}, {parts[0]}, ({parts[1]}) - ({parts[0]}))"

    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.slice\(([^)]*)\)", repl_slice, s)

    # localeCompare
    s = re.sub(
        r"(\$?[A-Za-z_][\w\[\]'\"\->]*)\.localeCompare\(([^)]+)\)",
        r"strcmp(\1, \2)",
        s,
    )

    # sort — simple numeric
    s = re.sub(
        r"(\$?[A-Za-z_][\w\->]*)\.sort\(\s*\(\s*([A-Za-z_]\w*)\s*,\s*([A-Za-z_]\w*)\s*\)\s*=>\s*\2\s*-\s*\3\s*\)",
        r"sort(\1)",
        s,
    )
    s = re.sub(
        r"(\$?[A-Za-z_][\w\->]*)\.sort\(\s*\(\s*([A-Za-z_]\w*)\s*,\s*([A-Za-z_]\w*)\s*\)\s*=>\s*\3\s*-\s*\2\s*\)",
        r"rsort(\1)",
        s,
    )
    # sort by a[0] - b[0]
    s = re.sub(
        r"(\$?[A-Za-z_][\w\->]*)\.sort\(\s*\(\s*([A-Za-z_]\w*)\s*,\s*([A-Za-z_]\w*)\s*\)\s*=>\s*\2\[0\]\s*-\s*\3\[0\]\s*\)",
        r"usort(\1, function($a, $b) { return $a[0] <=> $b[0]; })",
        s,
    )
    # sort by a.r - b.r  (may already be ['r'])
    s = re.sub(
        r"(\$?[A-Za-z_][\w\->]*)\.sort\(\s*\(\s*([A-Za-z_]\w*)\s*,\s*([A-Za-z_]\w*)\s*\)\s*=>\s*\2\.r\s*-\s*\3\.r\s*\)",
        r"usort(\1, function($a, $b) { return $a['r'] <=> $b['r']; })",
        s,
    )

    # length
    def repl_len(m):
        obj = m.group(1)
        # strip $
        name = obj
        if name.startswith("$this->"):
            return f"count({obj})"
        base = name.lstrip("$")
        # obj may be foo['idx']
        if "[" in base:
            return f"count({obj})"
        if base in string_vars:
            return f"strlen({obj})"
        return f"count({obj})"

    s = re.sub(r"(\$?[A-Za-z_][\w\->]*(?:\[[^\]]+\])*)\.length\b", repl_len, s)

    # remaining property access obj.prop → obj['prop'] (not methods, not $this->)
    def repl_prop(m):
        obj, prop = m.group(1), m.group(2)
        if prop in SKIP_METHODS:
            return m.group(0)
        if obj == "$this":
            return m.group(0)
        return f"{obj}['{prop}']"

    s = re.sub(r"(\$?[A-Za-z_][\w\->]*)\.([A-Za-z_]\w*)\b", repl_prop, s)

    return s


def dollarize_idents(s: str, extra_skip: set[str] | None = None) -> str:
    skip = KEYWORDS | PHP_BUILTINS | (extra_skip or set())
    # don't dollarize already-dollared, strings, comments

    out = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        # line comment
        if ch == "/" and i + 1 < n and s[i + 1] == "/":
            j = s.find("\n", i)
            if j < 0:
                out.append(s[i:])
                break
            out.append(s[i:j])
            i = j
            continue
        # string
        if ch in ("'", '"'):
            q = ch
            j = i + 1
            while j < n:
                if s[j] == "\\":
                    j += 2
                    continue
                if s[j] == q:
                    j += 1
                    break
                j += 1
            out.append(s[i:j])
            i = j
            continue
        # identifier
        if ch.isalpha() or ch == "_":
            j = i + 1
            while j < n and (s[j].isalnum() or s[j] == "_"):
                j += 1
            ident = s[i:j]
            # already has $ before?
            prev = out[-1] if out else ""
            if (
                ident in skip
                or ident.startswith("PHP_")
                or (prev and prev[-1] in ("$", ">", "\\"))
                or ident in ("function",)
            ):
                out.append(ident)
            else:
                # function call of unknown helper (closure vars already $)
                out.append("$" + ident)
            i = j
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def convert_for_of(s: str, string_vars: set[str]) -> str:
    def repl(m):
        var, coll = m.group(1), m.group(2)
        cname = coll.lstrip("$")
        if cname in string_vars:
            return f"foreach (str_split({coll}) as ${var})"
        return f"foreach ({coll} as ${var})"

    s = re.sub(r"for\s*\(\s*(?:const|let|var)\s+(\w+)\s+of\s+([^)]+)\)", repl, s)
    return s


def convert_for_let(s: str) -> str:
    s = re.sub(r"for\s*\(\s*(?:let|const|var)\s+", "for (", s)
    return s


def convert_decls(s: str) -> str:
    # const/let/var a = ...  or  const a, b
    def repl(m):
        rest = m.group(1)
        return rest

    s = re.sub(r"\b(?:const|let|var)\s+", "", s)
    return s


def convert_undefined(s: str) -> str:
    s = s.replace("undefined", "null")
    s = s.replace("!== null", "!== null")
    return s


def convert_body(body: str, params: list[str], string_vars: set[str]) -> str:
    nested = find_nested_fns(body)
    nested_names = [n[0] for n in nested]
    outer_vars = collect_outer_vars(body, params, nested_names)

    # replace nested fns from the end so offsets stay valid
    pieces = []
    last = 0
    # work left to right building replacements
    repls = []
    for name, args, nbody, a, b in nested:
        inner_string = set(string_vars)
        for p in args:
            if p in STRING_HINTS:
                inner_string.add(p)
        converted_inner = convert_body_simple(nbody, args + outer_vars, inner_string)
        use_vars = [v for v in outer_vars if v != name]
        # include other nested names for mutual recursion
        for nn in nested_names:
            if nn not in use_vars and nn != name:
                use_vars.append(nn)
        use_list = ", ".join(f"&${v}" for v in use_vars)
        arg_list = ", ".join(f"${a}" for a in args)
        # recursive self
        if name not in [x.split("$")[-1] if False else name for x in use_vars]:
            if name not in [u.lstrip("&$") for u in []]:
                pass
        if name not in use_vars:
            use_vars2 = use_vars + [name]
        else:
            use_vars2 = use_vars
        use_list = ", ".join(f"&${v}" for v in use_vars2)
        php_fn = f"${name} = function({arg_list}) use ({use_list}) {{\n{converted_inner}\n    }}"
        repls.append((a, b, php_fn))

    if repls:
        out = []
        pos = 0
        for a, b, php_fn in repls:
            out.append(body[pos:a])
            out.append(php_fn)
            pos = b
            # drop trailing semicolon if present — we'll add
            if pos < len(body) and body[pos] == ";":
                pos += 1
            php_fn_with = php_fn  # already
        out.append(body[pos:])
        body = "".join(out)
        # The inserted php_fn is already converted; remaining JS needs convert
        # Split by the php_fn markers — messy because convert would re-dollarize
        # Instead: convert the leftover JS parts only
        # Rebuild: convert_body_simple on original with nested replaced by placeholders
        body_ph = []
        pos = 0
        placeholders = {}
        # re-do from original nested
        body_orig_parts = []
        # Use a cleaner approach below
        pass

    # Simpler path: if nested, convert whole body then fix function headers
    return finalize_body(body if not repls else reconstruct(body, params, string_vars, nested), params, string_vars, nested)


def reconstruct(body_unused, params, string_vars, nested):
    # unused
    return ""


def convert_body_simple(body: str, scope_vars: list[str], string_vars: set[str]) -> str:
    s = body
    s = dollarize_expr(s, string_vars)
    s = convert_for_of(s, string_vars)
    s = convert_for_let(s)
    s = convert_decls(s)
    s = convert_methods(s, string_vars)
    s = convert_undefined(s)
    s = dollarize_idents(s)
    # fix double dollars
    s = s.replace("$$", "$")
    # fix $this
    s = s.replace("$$this", "$this")
    # true/false already keywords
    # fix $max( $min( etc if dollarize hit builtins after Math replace — builtins skipped
    # fix $array_fill
    return indent_block(s, 2)


def indent_block(s: str, extra: int) -> str:
    lines = s.splitlines()
    out = []
    for line in lines:
        if line.strip() == "":
            out.append("")
        else:
            # keep existing indent, add 4 spaces if needed
            out.append(line)
    return "\n".join(out)


def finalize_body(body, params, string_vars, nested):
    # This function is leftover; use convert_full_body
    return convert_full_body(body, params, string_vars)


def convert_full_body(body: str, params: list[str], string_vars: set[str]) -> str:
    nested = find_nested_fns(body)
    if not nested:
        return convert_body_simple(body, params, string_vars)

    # Replace nested with placeholders, convert outer, convert inners, splice
    ph = {}
    tmp = body
    # replace from end
    for idx, (name, args, nbody, a, b) in enumerate(sorted(nested, key=lambda x: -x[3])):
        key = f"__NESTED_{idx}__"
        # include trailing ;
        end = b
        if end < len(tmp) and tmp[end] == ";":
            end += 1
        ph[key] = (name, args, nbody)
        tmp = tmp[:a] + key + tmp[end:]

    outer_vars = collect_outer_vars(body, params, [n[0] for n in nested])
    outer_php = convert_body_simple(tmp, params, string_vars)

    for idx, (name, args, nbody, a, b) in enumerate(sorted(nested, key=lambda x: -x[3])):
        key = f"__NESTED_{idx}__"
        key_php = "$" + key if False else key
        # after dollarize, placeholder may become $__NESTED_0__
        inner_string = set(string_vars)
        for p in args:
            if p in STRING_HINTS:
                inner_string.add(p)
        inner_php = convert_body_simple(nbody, args + outer_vars, inner_string)
        use_vars = list(outer_vars)
        for nn in [n[0] for n in nested]:
            if nn not in use_vars:
                use_vars.append(nn)
        if name not in use_vars:
            use_vars.append(name)
        use_list = ", ".join(f"&${v}" for v in use_vars)
        arg_list = ", ".join(f"${x}" for x in args)
        php_fn = f"${name} = function({arg_list}) use ({use_list}) {{\n{inner_php}\n        }}"
        outer_php = outer_php.replace("$" + key, php_fn)
        outer_php = outer_php.replace(key, php_fn)
    return outer_php


def convert_class_body(cbody: str, class_name: str) -> str:
    # constructor
    cbody = strip_jsdoc(cbody)
    # methods: name(args) { }
    methods = []
    i = 0
    while i < len(cbody):
        m = re.match(r"\s*(\w+)\s*\(([^)]*)\)\s*\{", cbody[i:])
        if not m:
            i += 1
            continue
        name = m.group(1)
        args = [a.strip() for a in m.group(2).split(",") if a.strip()]
        start = i + m.end()
        depth = 1
        j = start
        while j < len(cbody):
            if cbody[j] == "{":
                depth += 1
            elif cbody[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        body = cbody[start:j]
        php_name = "__construct" if name == "constructor" else name
        string_vars = {p for p in args if p in STRING_HINTS}
        # formula, cell are strings
        php_body = convert_full_body(body, args, string_vars)
        arg_list = ", ".join(f"${a}" for a in args)
        methods.append(f"    function {php_name}({arg_list}) {{\n{php_body}\n    }}")
        i = j + 1
    # properties from this.x assignments
    props = set(re.findall(r"this\.(\w+)", cbody))
    prop_decl = "".join(f"    public ${p};\n" for p in sorted(props))
    return prop_decl + "\n" + "\n\n".join(methods)


def slug_title(js: str, folder: str) -> tuple[str, str]:
    title, url = js_header(js)
    if not title:
        num = int(folder.split("_")[0])
        t = folder.split("_", 1)[1].replace("_", " ").title()
        title = f"// LeetCode {num} - {t}"
    if not url:
        slug = folder.split("_", 1)[1].replace("_", "-")
        url = f"// https://leetcode.com/problems/{slug}/"
    return title, url


def convert_file(folder: str) -> str:
    d = ROOT / folder
    js = (d / "solution.js").read_text()
    cfg = json.loads((d / "tests/config.json").read_text())
    title, url = slug_title(js, folder)
    js_clean = strip_jsdoc(js)

    cls = extract_class(js_clean)
    if cls:
        cname, cbody = cls
        body = convert_class_body(cbody, cname)
        return f"<?php\n{title}\n{url}\n\nclass {cname} {{\n{body}\n}}\n"

    main = extract_main(js_clean)
    if not main:
        raise RuntimeError(f"no main in {folder}")
    name, args, body = main
    cfg_method = cfg.get("method", name)
    if cfg_method in ("solve", "__init__", "TreeNode", "ListNode"):
        method = name
    else:
        method = cfg_method if cfg_method == name else name

    string_vars = {p for p in args if p in STRING_HINTS}
    php_body = convert_full_body(body, args, string_vars)
    arg_list = ", ".join(f"${a}" for a in args)
    return (
        f"<?php\n{title}\n{url}\n\n"
        f"class Solution {{\n"
        f"    function {method}({arg_list}) {{\n"
        f"{php_body}\n"
        f"    }}\n"
        f"}}\n"
    )


def main():
    ok = 0
    fail = []
    for folder in BATCH:
        try:
            php = convert_file(folder)
            (ROOT / folder / "solution.php").write_text(php, encoding="utf-8")
            ok += 1
        except Exception as e:
            fail.append((folder, str(e)))
            print("FAIL", folder, e)
    print(f"wrote {ok}, failed {len(fail)}")


if __name__ == "__main__":
    main()
