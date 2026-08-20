#!/usr/bin/env python3
"""Port stub solution.ts files in 1500-1699 from solution.js. Temporary helper."""

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
    "object": "Record<string, unknown>",
    "Object": "Record<string, unknown>",
    "Array": "any[]",
    "TreeNode": "TreeNode | null",
    "ListNode": "ListNode | null",
    "Node": "Node",
    "narynode": "Node",
    "NaryNode": "Node",
    "SparseVector": "SparseVector",
    "ArrayReader": "any",
}


def is_sql(folder: Path) -> bool:
    cases = folder / "tests" / "cases.json"
    if cases.exists():
        text = cases.read_text(encoding="utf-8")
        if re.search(r'"kind"\s*:\s*"sql"', text):
            return True
    return (folder / "solution.sql").exists()


def is_ts_stub(text: str) -> bool:
    if re.search(r"function\s+solve\s*\([^)]*\)\s*:\s*unknown", text):
        return True
    if "Not implemented" in text:
        return True
    if re.search(r"function\s+\w+\s*\([^)]*\)\s*:\s*unknown\s*\{\s*return\s+null", text):
        return True
    return False


def map_jsdoc_type(raw: str | None) -> str:
    if not raw:
        return "any"
    raw = raw.strip().strip("{}").strip()
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
        return f"{map_jsdoc_type(raw[:-2])}[]"
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


def extract_header(js: str) -> tuple[str, str]:
    lines = js.splitlines(True)
    header_lines: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("//") or line.strip() == "":
            header_lines.append(line)
            i += 1
            if line.strip() == "" and header_lines and any(l.startswith("//") for l in header_lines):
                # stop after first blank line following comments
                break
            continue
        break
    # trim trailing blanks except one
    while len(header_lines) > 1 and header_lines[-1].strip() == "" and header_lines[-2].strip() == "":
        header_lines.pop()
    if header_lines and header_lines[-1].strip() != "":
        header_lines.append("\n")
    header = "".join(header_lines)
    return header, js[len("".join(lines[:i])) :] if False else js[sum(len(x) for x in lines[:i]) :]


def extract_header2(js: str) -> tuple[str, str]:
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


def type_params(params_raw: str, param_types: dict[str, str]) -> str:
    typed = []
    if not params_raw.strip():
        return ""
    for p in params_raw.split(","):
        p = p.strip()
        if not p:
            continue
        if "=" in p:
            pname, default = [x.strip() for x in p.split("=", 1)]
            ptype = param_types.get(pname, "any")
            typed.append(f"{pname}: {ptype} = {default}")
        else:
            ptype = param_types.get(p, "any")
            typed.append(f"{p}: {ptype}")
    return ", ".join(typed)


def convert_var_functions(js: str) -> str:
    result: list[str] = []
    i = 0
    pattern = re.compile(
        r"(?P<jsdoc>/\*\*[\s\S]*?\*/\s*)?var\s+(?P<name>\w+)\s*=\s*function\s*\((?P<params>[^)]*)\)\s*\{"
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

        param_types: dict[str, str] = {}
        ret_type = "any"
        if jd:
            plist, ret = parse_jsdoc_block(jd)
            param_types = {n: t for n, t in plist}
            if ret:
                ret_type = ret

        body_start = m.end() - 1
        body_end = find_matching_brace(js, body_start)
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
        result.append(f"function {name}({params}): {ret_type} {{{body}}}")
        i = k
    return "".join(result)


def convert_js_class(js: str, class_props: dict[str, str] | None = None) -> str:
    js = re.sub(r"\n?module\.exports\s*=\s*\{[^}]+\};?\s*", "\n", js)
    js = re.sub(r"(?m)^class\s+(\w+)", r"export class \1", js)

    m = re.search(r"export class\s+(\w+)\s*\{", js)
    if not m:
        return js
    class_name = m.group(1)
    open_idx = m.end() - 1
    close_idx = find_matching_brace(js, open_idx)
    before = js[: m.start()]
    after = js[close_idx + 1 :]
    body = js[open_idx + 1 : close_idx]

    # Rewrite only top-level methods: constructor / identifier not in CONTROL
    # Scan body for method-like patterns at brace depth 0
    out_body: list[str] = []
    i = 0
    depth = 0
    in_str = None
    escape = False
    method_start_re = re.compile(
        r"(?:/\*\*[\s\S]*?\*/\s*)?(constructor|[A-Za-z_]\w*)\s*\(([^)]*)\)\s*\{"
    )

    while i < len(body):
        # Only look for methods at depth 0
        if depth == 0 and in_str is None:
            m2 = method_start_re.match(body, i)
            if m2:
                name = m2.group(1)
                if name not in CONTROL:
                    # parse jsdoc
                    jsdoc = ""
                    jdm = re.match(r"/\*\*([\s\S]*?)\*/\s*", body[i : m2.end()])
                    if jdm:
                        jsdoc = "/**" + jdm.group(1) + "*/"
                    params_raw = m2.group(2)
                    plist, ret = parse_jsdoc_block(jsdoc) if jsdoc else ([], None)
                    param_types = {n: t for n, t in plist}
                    params = type_params(params_raw, param_types)
                    brace_idx = m2.end() - 1
                    end = find_matching_brace(body, brace_idx)
                    method_body = body[brace_idx + 1 : end]
                    if name == "constructor":
                        out_body.append(f"constructor({params}) {{{method_body}}}")
                    else:
                        rtype = ret or "any"
                        out_body.append(f"{name}({params}): {rtype} {{{method_body}}}")
                    i = end + 1
                    continue
        # copy one char / track depth
        ch = body[i]
        if in_str:
            out_body.append(ch)
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
            out_body.append(ch)
            i += 1
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        out_body.append(ch)
        i += 1

    props_block = ""
    if class_props:
        props_block = "".join(f"    {k}: {v};\n" for k, v in class_props.items()) + "\n"

    # Clean leftover jsdoc in body
    new_body = "".join(out_body)
    new_body = re.sub(r"/\*\*[\s\S]*?\*/\s*", "", new_body)
    return before + f"export class {class_name} {{\n{props_block}{new_body}}}\n" + after


def convert_node_helper(js: str) -> str:
    pattern = re.compile(r"/\*\*[\s\S]*?\*/\s*function\s+Node\s*\([^)]*\)\s*\{[\s\S]*?\n\}")
    repl = (
        "class Node {\n"
        "    val: string;\n"
        "    left: Node | null;\n"
        "    right: Node | null;\n"
        "    constructor(val?: string, left?: Node | null, right?: Node | null) {\n"
        '        this.val = val === undefined ? " " : val;\n'
        "        this.left = left === undefined ? null : left;\n"
        "        this.right = right === undefined ? null : right;\n"
        "    }\n"
        "}"
    )
    return pattern.sub(repl, js)


def convert_sparse_vector(header: str) -> str:
    return (
        header
        + "export class SparseVector {\n"
        + "    values: Map<number, number>;\n\n"
        + "    constructor(nums: number[]) {\n"
        + "        this.values = new Map();\n"
        + "        for (let i = 0; i < nums.length; i++) {\n"
        + "            if (nums[i]) this.values.set(i, nums[i]);\n"
        + "        }\n"
        + "    }\n\n"
        + "    dotProduct(vec: SparseVector): number {\n"
        + "        if (this.values.size > vec.values.size) return vec.dotProduct(this);\n"
        + "        let sum = 0;\n"
        + "        for (const [i, x] of this.values) {\n"
        + "            if (vec.values.has(i)) sum += x * vec.values.get(i)!;\n"
        + "        }\n"
        + "        return sum;\n"
        + "    }\n"
        + "}\n\n"
        + "function dotProduct(nums1: number[], nums2: number[]): number {\n"
        + "    return new SparseVector(nums1).dotProduct(new SparseVector(nums2));\n"
        + "}\n"
    )


CLASS_PROPS = {
    "1500_design_a_file_sharing_system": {
        "owners": "Map<number, Set<number>>",
        "chunks": "Map<number, Set<number>>",
        "free": "number[]",
        "nextId": "number",
    },
    "1586_binary_search_tree_iterator_ii": {
        "values": "number[]",
        "index": "number",
    },
}


def add_ambient_types(ts: str, folder_name: str) -> str:
    extras: list[str] = []
    if "TreeNode" in ts and "class TreeNode" not in ts and "interface TreeNode" not in ts:
        extras.append(
            "interface TreeNode {\n    val: number;\n    left: TreeNode | null;\n    right: TreeNode | null;\n}\n"
        )
    if "ListNode" in ts and "class ListNode" not in ts and "interface ListNode" not in ts:
        extras.append(
            "interface ListNode {\n    val: number;\n    next: ListNode | null;\n}\n"
        )
    # N-ary Node
    if (
        re.search(r"\bNode\b", ts)
        and "class Node" not in ts
        and "interface Node" not in ts
    ):
        if "children" in ts or folder_name.startswith(("1506_", "1516_", "1522_")):
            extras.append("interface Node {\n    val: number;\n    children: Node[];\n}\n")
    if not extras:
        return ts
    m = re.match(r"((?://[^\n]*\n)+\n*)", ts)
    if m:
        return m.group(1) + "\n".join(extras) + "\n" + ts[m.end() :]
    return "\n".join(extras) + "\n" + ts


def refine_types_from_config(ts: str, folder: Path) -> str:
    """Fill remaining `any` types from config when JSDoc was missing."""
    cfg_path = folder / "tests" / "config.json"
    if not cfg_path.exists():
        return ts
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8").lstrip("\ufeff"))
    except Exception:
        return ts
    types = cfg.get("types") or {}
    method = cfg.get("method")
    if not method or not isinstance(types, dict):
        return ts

    # Replace return any
    ret = types.get("return")
    if isinstance(ret, str):
        ts_ret = map_jsdoc_type(ret)
        pattern = re.compile(rf"(function\s+{re.escape(method)}\s*\([^)]*\))\s*:\s*any\b")
        ts = pattern.sub(rf"\1: {ts_ret}", ts, count=1)

    # Replace param any using paramOrder
    param_order = cfg.get("paramOrder") or []
    if param_order:
        m = re.search(rf"function\s+{re.escape(method)}\s*\(([^)]*)\)\s*:", ts)
        if m:
            raw_params = m.group(1)
            parts = [p.strip() for p in raw_params.split(",") if p.strip()]
            new_parts = []
            for idx, part in enumerate(parts):
                pname = part.split(":")[0].strip().split("=")[0].strip()
                if ": any" in part and idx < len(param_order):
                    key = param_order[idx]
                    if key in types and isinstance(types[key], str):
                        ptype = map_jsdoc_type(types[key])
                        default = ""
                        if "=" in part:
                            default = " = " + part.split("=", 1)[1].strip()
                        new_parts.append(f"{pname}: {ptype}{default}")
                        continue
                new_parts.append(part)
            ts = ts[: m.start(1)] + ", ".join(new_parts) + ts[m.end(1) :]
    return ts


def fix_common_types(ts: str) -> str:
    # Node[] params wrongly becoming Node | null[]
    ts = ts.replace("tree: Node | null[]", "tree: Node[]")
    ts = ts.replace("tree: Node[] | null", "tree: Node[]")
    # For findRoot return Node | null is fine; param should be Node[]
    return ts


def convert_js_to_ts(js: str, folder_name: str) -> str:
    js = js.lstrip("\ufeff")
    header, body = extract_header2(js)

    if folder_name.startswith("1570_"):
        return convert_sparse_vector(header)

    props = CLASS_PROPS.get(folder_name)

    if re.search(r"(?m)^class\s+\w+", body) or re.search(r"(?m)^export class\s+\w+", body):
        converted = convert_js_class(body, props)
        converted = re.sub(r"/\*\*[\s\S]*?\*/\s*", "", converted)
        converted = re.sub(r"\n{3,}", "\n\n", converted).strip() + "\n"
        return header + converted

    if re.search(r"function\s+Node\s*\(", body):
        body = convert_node_helper(body)

    if re.search(r"var\s+\w+\s*=\s*function", body):
        converted = convert_var_functions(body)
    else:
        converted = body

    converted = re.sub(r"/\*\*[\s\S]*?\*/\s*", "", converted)
    converted = re.sub(r"\n{3,}", "\n\n", converted).strip() + "\n"
    return header + converted


def port_folder(folder: Path) -> str:
    js_path = folder / "solution.js"
    ts_path = folder / "solution.ts"
    js = js_path.read_text(encoding="utf-8")
    ts = convert_js_to_ts(js, folder.name)
    ts = refine_types_from_config(ts, folder)
    ts = add_ambient_types(ts, folder.name)
    ts = fix_common_types(ts)
    ts = ts.replace("\r\n", "\n").replace("\ufeff", "")
    ts_path.write_text(ts, encoding="utf-8")
    return "ok"


def list_targets(force_all_ported: bool = True) -> list[Path]:
    """Re-port all non-SQL 1500-1599 that have JS, plus any remaining stubs in 1600-1699."""
    targets: list[Path] = []
    for folder in sorted(ROOT.iterdir()):
        if not folder.is_dir():
            continue
        m = re.match(r"^(1[5-6]\d{2})_", folder.name)
        if not m:
            continue
        num = int(m.group(1))
        if is_sql(folder):
            continue
        ts_path = folder / "solution.ts"
        js_path = folder / "solution.js"
        if not js_path.exists() or not ts_path.exists():
            continue
        text = ts_path.read_text(encoding="utf-8")
        if num < 1600:
            # Always re-port 1500-1599 non-SQL from JS (fix previous bad ports)
            if force_all_ported or is_ts_stub(text):
                # Only if previously was in stub set or looks like our port / stub
                targets.append(folder)
        elif is_ts_stub(text):
            targets.append(folder)
    return targets


def main() -> None:
    # Exact list from original survey of stubs (non-SQL)
    stub_names = [
        "1500_design_a_file_sharing_system",
        "1502_can_make_arithmetic_progression_from_sequence",
        "1503_last_moment_before_all_ants_fall_out_of_a_plank",
        "1504_count_submatrices_with_all_ones",
        "1505_minimum_possible_integer_after_at_most_k_adjacent_swaps_on_digits",
        "1506_find_root_of_n_ary_tree",
        "1507_reformat_date",
        "1508_range_sum_of_sorted_subarray_sums",
        "1509_minimum_difference_between_largest_and_smallest_value_in_three_moves",
        "1510_stone_game_iv",
        "1512_number_of_good_pairs",
        "1513_number_of_substrings_with_only_1s",
        "1514_path_with_maximum_probability",
        "1515_best_position_for_a_service_centre",
        "1516_move_sub_tree_of_n_ary_tree",
        "1518_water_bottles",
        "1519_number_of_nodes_in_the_sub_tree_with_the_same_label",
        "1520_maximum_number_of_non_overlapping_substrings",
        "1521_find_a_value_of_a_mysterious_function_closest_to_target",
        "1522_diameter_of_n_ary_tree",
        "1523_count_odd_numbers_in_an_interval_range",
        "1524_number_of_sub_arrays_with_odd_sum",
        "1525_number_of_good_ways_to_split_a_string",
        "1526_minimum_number_of_increments_on_subarrays_to_form_a_target_array",
        "1528_shuffle_string",
        "1529_minimum_suffix_flips",
        "1530_number_of_good_leaf_nodes_pairs",
        "1531_string_compression_ii",
        "1533_find_the_index_of_the_large_integer",
        "1534_count_good_triplets",
        "1535_find_the_winner_of_an_array_game",
        "1536_minimum_swaps_to_arrange_a_binary_grid",
        "1537_get_the_maximum_score",
        "1538_guess_the_majority_in_a_hidden_array",
        "1539_kth_missing_positive_number",
        "1540_can_convert_string_in_k_moves",
        "1541_minimum_insertions_to_balance_a_parentheses_string",
        "1542_find_longest_awesome_substring",
        "1544_make_the_string_great",
        "1545_find_kth_bit_in_nth_binary_string",
        "1546_maximum_number_of_non_overlapping_subarrays_with_sum_equals_target",
        "1547_minimum_cost_to_cut_a_stick",
        "1548_the_most_similar_path_in_a_graph",
        "1550_three_consecutive_odds",
        "1551_minimum_operations_to_make_array_equal",
        "1552_magnetic_force_between_two_balls",
        "1553_minimum_number_of_days_to_eat_n_oranges",
        "1554_strings_differ_by_one_character",
        "1556_thousand_separator",
        "1557_minimum_number_of_vertices_to_reach_all_nodes",
        "1558_minimum_numbers_of_function_calls_to_make_target_array",
        "1559_detect_cycles_in_2d_grid",
        "1560_most_visited_sector_in_a_circular_track",
        "1561_maximum_number_of_coins_you_can_get",
        "1562_find_latest_group_of_size_m",
        "1563_stone_game_v",
        "1564_put_boxes_into_the_warehouse_i",
        "1566_detect_pattern_of_length_m_repeated_k_or_more_times",
        "1567_maximum_length_of_subarray_with_positive_product",
        "1568_minimum_number_of_days_to_disconnect_island",
        "1569_number_of_ways_to_reorder_array_to_get_same_bst",
        "1570_dot_product_of_two_sparse_vectors",
        "1572_matrix_diagonal_sum",
        "1573_number_of_ways_to_split_a_string",
        "1574_shortest_subarray_to_be_removed_to_make_array_sorted",
        "1575_count_all_possible_routes",
        "1576_replace_all_s_to_avoid_consecutive_repeating_characters",
        "1577_number_of_ways_where_square_of_number_is_equal_to_product_of_two_numbers",
        "1578_minimum_time_to_make_rope_colorful",
        "1579_remove_max_number_of_edges_to_keep_graph_fully_traversable",
        "1580_put_boxes_into_the_warehouse_ii",
        "1582_special_positions_in_a_binary_matrix",
        "1583_count_unhappy_friends",
        "1584_min_cost_to_connect_all_points",
        "1585_check_if_string_is_transformable_with_substring_sort_operations",
        "1586_binary_search_tree_iterator_ii",
        "1588_sum_of_all_odd_length_subarrays",
        "1589_maximum_sum_obtained_of_any_permutation",
        "1590_make_sum_divisible_by_p",
        "1591_strange_printer_ii",
        "1592_rearrange_spaces_between_words",
        "1593_split_a_string_into_the_max_number_of_unique_substrings",
        "1594_maximum_non_negative_product_in_a_matrix",
        "1595_minimum_cost_to_connect_two_groups_of_points",
        "1597_build_binary_expression_tree_from_infix_expression",
        "1598_crawler_log_folder",
        "1599_maximum_profit_of_operating_a_centennial_wheel",
    ]

    print(f"Re-porting {len(stub_names)} folders...")
    for name in stub_names:
        folder = ROOT / name
        status = port_folder(folder)
        print(f"{status} {name}")

    remaining = []
    for folder in sorted(ROOT.iterdir()):
        if not folder.is_dir() or not re.match(r"^1[5-6]\d{2}_", folder.name):
            continue
        ts_path = folder / "solution.ts"
        if not ts_path.exists():
            continue
        text = ts_path.read_text(encoding="utf-8")
        if is_ts_stub(text) and not is_sql(folder):
            remaining.append(folder.name)
    print(f"Remaining non-SQL stubs: {len(remaining)}")
    for name in remaining:
        print(f"  STILL-STUB {name}")


if __name__ == "__main__":
    main()
