#!/usr/bin/env python3
"""Compile and run C++ LeetCode solution tests."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

RUNNERS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RUNNERS_DIR / "common"))
from test_utils import load_problem_tests, run_design_cases, uses_design_cases  # noqa: E402
from runner_policy import pre_run_check, print_skip  # noqa: E402


def cpp_literal(value):
    if value is None:
        return "nullptr"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return str(value)
    if isinstance(value, str):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    if isinstance(value, list):
        if not value:
            return "std::vector<int>{}"
        if all(isinstance(item, bool) for item in value):
            items = ", ".join("true" if item else "false" for item in value)
            return f"std::vector<bool>{{{items}}}"
        if all(isinstance(item, int) for item in value):
            items = ", ".join(str(item) for item in value)
            return f"std::vector<int>{{{items}}}"
        if all(isinstance(item, (int, float)) for item in value):
            items = ", ".join(str(float(item)) for item in value)
            return f"std::vector<double>{{{items}}}"
        if all(isinstance(item, str) for item in value):
            items = ", ".join(cpp_literal(item) for item in value)
            return f"std::vector<std::string>{{{items}}}"
        if all(isinstance(item, list) for item in value):
            if value and all(
                isinstance(cell, str) and len(cell) == 1 for row in value for cell in row
            ):
                rows = ", ".join(
                    "std::vector<char>{" + ", ".join(f"'{cell}'" for cell in row) + "}"
                    for row in value
                )
                return f"std::vector<std::vector<char>>{{{rows}}}"
            if all(isinstance(cell, str) for row in value for cell in row):
                rows = ", ".join(cpp_literal(row) for row in value)
                return f"std::vector<std::vector<std::string>>{{{rows}}}"
            rows = ", ".join(cpp_literal(row) for row in value)
            return f"std::vector<std::vector<int>>{{{rows}}}"
    raise TypeError(f"Unsupported C++ literal type: {type(value)!r}")


def cpp_tree_literal(value: list) -> str:
    items = []
    for item in value:
        if item is None:
            items.append("std::nullopt")
        else:
            items.append(f"std::optional<int>{{{item}}}")
    return "std::vector<std::optional<int>>{" + ", ".join(items) + "}"


def build_check(
    index: int,
    method_name: str,
    arg_names: list[str],
    expected,
    arg_types: dict,
    args: dict | None = None,
    class_name: str = "Solution",
) -> str:
    prelude = ""
    if method_name == "cleanRoom" and args and "room" in args:
        room = cpp_literal(args["room"])
        row = args["row"]
        col = args["col"]
        expected_expr = cpp_literal(expected)
        check = f'runCleanRoom(solution, {room}, {row}, {col}) == {expected_expr}'
    elif (
        class_name == "Codec"
        and args
        and ("url" in args or "longUrl" in args)
    ):
        long_url = args.get("url") or args.get("longUrl")
        expected_expr = cpp_literal(expected)
        check = f"codec.decode(codec.encode({cpp_literal(long_url)})) == {expected_expr}"
    elif arg_types.get("return") == "void" and args and "root" in args:
        prelude = (
            f"TreeNode* root = to_tree({cpp_tree_literal(args['root'])});\n"
            f"            solution.{method_name}(root);"
        )
        expected_expr = cpp_tree_literal(expected)
        check = f"tree_lists_equal(tree_to_list(root), {expected_expr})"
    else:
        call_args = ", ".join(arg_names)
        call = f"solution.{method_name}({call_args})"
        if arg_types.get("return") == "listnode":
            expected_expr = f"to_vector(to_listnode({cpp_literal(expected)}))"
            actual_expr = f"to_vector(from_listnode({call}))"
            check = f"vectors_equal({actual_expr}, {expected_expr})"
        elif arg_types.get("return") == "treenode":
            expected_expr = cpp_tree_literal(expected)
            check = f"tree_lists_equal(tree_to_list({call}), {expected_expr})"
        elif isinstance(expected, float) or (
            isinstance(expected, list)
            and expected
            and all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in expected)
            and any(isinstance(item, float) for item in expected)
        ):
            expected_expr = cpp_literal(expected)
            check = f"approx_equal({call}, {expected_expr})"
        else:
            expected_expr = cpp_literal(expected)
            check = f"{call} == {expected_expr}"
    body = f"{prelude}\n            if ({check})" if prelude else f"if ({check})"
    return textwrap.dedent(
        f"""
        {{
            {body} {{
                ++passed;
                std::cout << "  PASS case {index}\\n";
            }} else {{
                std::cout << "  FAIL case {index}\\n";
            }}
        }}
        """
    ).strip()


def build_main_source(config: dict, cases_doc: dict) -> str:
    method_name = config["method"]
    class_name = config.get("class", "Solution")
    param_order = config.get("paramOrder") or (
        list(cases_doc["cases"][0]["args"].keys()) if cases_doc.get("cases") else []
    )
    arg_types = config.get("types") or {}

    case_blocks = []
    uses_robot = method_name == "cleanRoom"
    uses_tree = arg_types.get("return") in {"treenode", "void"} or any(
        arg_types.get(key) == "treenode" for key in param_order
    )
    for index, case in enumerate(cases_doc.get("cases", []), start=1):
        args = case["args"]
        if "room" in args:
            uses_robot = True
        if "root" in args or arg_types.get("return") == "treenode":
            uses_tree = True
        arg_exprs = []
        arg_names = []
        setup_lines = []
        for key_index, key in enumerate(param_order):
            if key not in args:
                continue
            value = args[key]
            if arg_types.get(key) == "listnode":
                expr = f"to_listnode({cpp_literal(value)})"
            elif arg_types.get(key) == "treenode":
                expr = f"to_tree({cpp_tree_literal(value)})"
            else:
                expr = cpp_literal(value)
            var_name = f"arg{index}_{key_index}"
            setup_lines.append(f"auto {var_name} = {expr};")
            arg_names.append(var_name)
        prelude = "\n            ".join(setup_lines)
        case_blocks.append(
            build_check(
                index,
                method_name,
                arg_names,
                case["expected"],
                arg_types,
                args,
                class_name,
            ).replace(
                "if (",
                f"{prelude}\n            if (",
                1,
            ) if prelude and not (
                (class_name == "Codec" and ("url" in args or "longUrl" in args))
                or (arg_types.get("return") == "void" and "root" in args)
                or (method_name == "cleanRoom" and "room" in args)
            ) else build_check(
                index,
                method_name,
                arg_names,
                case["expected"],
                arg_types,
                args,
                class_name,
            )
        )

    cases_joined = "\n        ".join(case_blocks) if case_blocks else 'std::cout << "  SKIP no test cases\\n";'

    robot_helpers = ""
    if uses_robot:
        robot_helpers = textwrap.dedent(
            """
            class Robot {
            public:
                virtual bool move() = 0;
                virtual void turnLeft() = 0;
                virtual void turnRight() = 0;
                virtual void clean() = 0;
                virtual ~Robot() = default;
            };

            class MockRobot : public Robot {
                std::vector<std::vector<int>> room_;
                int row_;
                int col_;
                int direction_ = 0;
                std::set<std::string> cleaned_;
                static constexpr int directions_[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

            public:
                MockRobot(const std::vector<std::vector<int>>& room, int row, int col)
                    : room_(room), row_(row), col_(col) {}

                bool move() override {
                    const int nextRow = row_ + directions_[direction_][0];
                    const int nextCol = col_ + directions_[direction_][1];
                    if (nextRow >= 0 && nextRow < static_cast<int>(room_.size()) && nextCol >= 0 &&
                        nextCol < static_cast<int>(room_[0].size()) && room_[nextRow][nextCol] == 1) {
                        row_ = nextRow;
                        col_ = nextCol;
                        return true;
                    }
                    return false;
                }

                void turnLeft() override { direction_ = (direction_ + 3) % 4; }
                void turnRight() override { direction_ = (direction_ + 1) % 4; }

                void clean() override {
                    cleaned_.insert(std::to_string(row_) + "," + std::to_string(col_));
                }

                bool allCleaned() const {
                    for (int r = 0; r < static_cast<int>(room_.size()); ++r) {
                        for (int c = 0; c < static_cast<int>(room_[r].size()); ++c) {
                            if (room_[r][c] == 1 &&
                                cleaned_.count(std::to_string(r) + "," + std::to_string(c)) == 0) {
                                return false;
                            }
                        }
                    }
                    return true;
                }
            };

            std::string runCleanRoom(
                Solution& solution,
                const std::vector<std::vector<int>>& room,
                int row,
                int col) {
                MockRobot robot(room, row, col);
                solution.cleanRoom(robot);
                return robot.allCleaned() ? "Robot cleaned all rooms." : "Robot missed rooms.";
            }
            """
        ).strip()

    extra_includes = "#include <set>\n        " if uses_robot else ""
    tree_helpers = ""
    if uses_tree:
        tree_helpers = textwrap.dedent(
            """
            #include <optional>
            #include <queue>

            TreeNode* to_tree(const std::vector<std::optional<int>>& values) {
                if (values.empty() || !values[0].has_value()) {
                    return nullptr;
                }
                TreeNode* root = new TreeNode(values[0].value());
                std::queue<TreeNode*> pending;
                pending.push(root);
                size_t index = 1;
                while (!pending.empty() && index < values.size()) {
                    TreeNode* node = pending.front();
                    pending.pop();
                    if (index < values.size() && values[index].has_value()) {
                        node->left = new TreeNode(values[index].value());
                        pending.push(node->left);
                    }
                    ++index;
                    if (index < values.size() && values[index].has_value()) {
                        node->right = new TreeNode(values[index].value());
                        pending.push(node->right);
                    }
                    ++index;
                }
                return root;
            }

            std::vector<std::optional<int>> tree_to_list(TreeNode* root) {
                std::vector<std::optional<int>> values;
                if (!root) {
                    return values;
                }
                std::queue<TreeNode*> pending;
                pending.push(root);
                while (!pending.empty()) {
                    TreeNode* node = pending.front();
                    pending.pop();
                    if (!node) {
                        values.push_back(std::nullopt);
                        continue;
                    }
                    values.push_back(node->val);
                    pending.push(node->left);
                    pending.push(node->right);
                }
                while (!values.empty() && !values.back().has_value()) {
                    values.pop_back();
                }
                return values;
            }

            bool tree_lists_equal(
                const std::vector<std::optional<int>>& left,
                const std::vector<std::optional<int>>& right) {
                return left == right;
            }
            """
        ).strip()

    instance_decl = "Codec codec;" if class_name == "Codec" else f"{class_name} solution;"

    return textwrap.dedent(
        f"""
        #include <iostream>
        #include <vector>
        #include <string>
        #include <cmath>
        {extra_includes}

        struct ListNode {{
            int val;
            ListNode *next;
            ListNode(int x) : val(x), next(nullptr) {{}}
        }};

        ListNode* to_listnode(const std::vector<int>& values) {{
            if (values.empty()) return nullptr;
            ListNode* head = new ListNode(values[0]);
            ListNode* current = head;
            for (size_t i = 1; i < values.size(); ++i) {{
                current->next = new ListNode(values[i]);
                current = current->next;
            }}
            return head;
        }}

        ListNode* from_listnode(ListNode* node) {{ return node; }}

        std::vector<int> to_vector(ListNode* node) {{
            std::vector<int> values;
            while (node) {{
                values.push_back(node->val);
                node = node->next;
            }}
            return values;
        }}

        bool vectors_equal(const std::vector<int>& a, const std::vector<int>& b) {{
            return a == b;
        }}

        bool approx_equal(double a, double b) {{
            return std::fabs(a - b) < 1e-5;
        }}

        bool approx_equal(const std::vector<double>& a, const std::vector<double>& b) {{
            if (a.size() != b.size()) return false;
            for (size_t i = 0; i < a.size(); ++i) {{
                if (std::fabs(a[i] - b[i]) >= 1e-5) return false;
            }}
            return true;
        }}

        {robot_helpers}

        #include "solution.cpp"

        {tree_helpers}

        int main() {{
            {instance_decl}
            int passed = 0;
            int total = {len(cases_doc.get("cases", []))};
            std::cout << "C++ tests: {method_name}()\\n";
            {cases_joined}
            std::cout << "Result: " << passed << "/" << total << " passed\\n";
            return passed == total ? 0 : 1;
        }}
        """
    )


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: run_tests.py <problem_dir>")
        return 2

    problem_dir = Path(sys.argv[1]).resolve()
    config, cases_doc = load_problem_tests(problem_dir)

    can_run, exit_code, message = pre_run_check(
        "cpp",
        config,
        cases_doc,
        has_solution_file=(problem_dir / "solution.cpp").exists(),
        has_python_reference=(problem_dir / "solution.py").exists(),
        toolchain_available=shutil.which("g++") is not None,
    )
    if not can_run:
        print(f"C++ tests: {problem_dir.name}")
        print_skip(message)
        return exit_code

    print(f"C++ tests: {problem_dir.name} :: {config.get('method', '?')}()")

    if uses_design_cases(cases_doc) or config.get("kind") == "design":
        python_solution = problem_dir / "solution.py"
        if not python_solution.exists():
            print("  design problems require a Python reference implementation")
            return 2
        import importlib.util

        spec = importlib.util.spec_from_file_location("solution", python_solution)
        loaded = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(loaded)
        passed, total = run_design_cases(loaded, cases_doc)
        print("  NOTE: validated design cases using Python reference implementation")
        print(f"Result: {passed}/{total} passed")
        return 0 if passed == total else 1

    temp_dir = Path(tempfile.mkdtemp())
    try:
        shutil.copy2(problem_dir / "solution.cpp", temp_dir / "solution.cpp")
        (temp_dir / "main.cpp").write_text(build_main_source(config, cases_doc), encoding="utf-8")
        binary = temp_dir / "tests"
        subprocess.check_call(
            ["g++", "-std=c++17", "-O2", "-o", str(binary), str(temp_dir / "main.cpp")],
            cwd=temp_dir,
        )
        subprocess.check_call([str(binary)], cwd=temp_dir)
        return 0
    except subprocess.CalledProcessError:
        return 1
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
