#!/usr/bin/env python3
"""Generate and run a Java test harness for a LeetCode solution."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

RUNNERS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RUNNERS_DIR / "common"))
from test_utils import load_problem_tests, uses_design_cases  # noqa: E402
from runner_policy import pre_run_check, print_skip  # noqa: E402


def java_literal(value):
    if value is None:
        return "null"
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
            return "new int[0]"
        if all(isinstance(item, bool) for item in value):
            return "new boolean[] { " + ", ".join("true" if item else "false" for item in value) + " }"
        if all(isinstance(item, int) for item in value):
            return "new int[] { " + ", ".join(str(item) for item in value) + " }"
        if all(isinstance(item, str) for item in value):
            return "new String[] { " + ", ".join(java_literal(item) for item in value) + " }"
        if all(isinstance(item, list) for item in value):
            if all(isinstance(cell, int) and not isinstance(cell, bool) for item in value for cell in item):
                rows = ", ".join(
                    "{ " + ", ".join(str(cell) for cell in item) + " }" if item else "{}"
                    for item in value
                )
                return "new int[][] { " + rows + " }"
            if value and any(value) and all(
                isinstance(cell, str) and len(cell) == 1 for item in value for cell in item
            ):
                rows = ", ".join(
                    "{ " + ", ".join("'" + cell.replace("\\", "\\\\").replace("'", "\\'") + "'" for cell in item) + " }"
                    if item else "{}"
                    for item in value
                )
                return "new char[][] { " + rows + " }"
            if all(isinstance(cell, str) for item in value for cell in item):
                rows = ", ".join(
                    "{ " + ", ".join(java_literal(cell) for cell in item) + " }" if item else "{}"
                    for item in value
                )
                return "new String[][] { " + rows + " }"
            return "new Object[] { " + ", ".join(java_literal(item) for item in value) + " }"
        return "new Object[] { " + ", ".join(java_literal(item) for item in value) + " }"
    raise TypeError(f"Unsupported literal type: {type(value)!r}")


def java_deep_equals_helpers() -> str:
    return textwrap.dedent(
        """
        static String stringify(Object value) {
            if (value instanceof int[]) return Arrays.toString((int[]) value);
            if (value instanceof double[]) return Arrays.toString((double[]) value);
            if (value instanceof boolean[]) return Arrays.toString((boolean[]) value);
            if (value instanceof char[]) return Arrays.toString((char[]) value);
            if (value instanceof char[][]) return Arrays.deepToString((char[][]) value);
            if (value instanceof Object[]) return Arrays.deepToString((Object[]) value);
            return String.valueOf(value);
        }

        static boolean valuesEqual(Object actual, Object expected) {
            if (actual instanceof int[] && expected instanceof int[]) {
                return Arrays.equals((int[]) actual, (int[]) expected);
            }
            if (actual instanceof boolean[] && expected instanceof boolean[]) {
                return Arrays.equals((boolean[]) actual, (boolean[]) expected);
            }
            if (actual instanceof char[] && expected instanceof char[]) {
                return Arrays.equals((char[]) actual, (char[]) expected);
            }
            if (actual instanceof char[][] && expected instanceof char[][]) {
                return Arrays.deepEquals((char[][]) actual, (char[][]) expected);
            }
            if (actual instanceof Object[] && expected instanceof int[]) {
                return objectArrayIntArrayEquals((Object[]) actual, (int[]) expected);
            }
            if (actual instanceof double[] && expected instanceof double[]) {
                return arraysApproxEqual((double[]) actual, (double[]) expected);
            }
            if (actual instanceof double[] && expected instanceof Object[]) {
                return arrayObjectApproxEqual((double[]) actual, (Object[]) expected);
            }
            if (actual instanceof Object[] && expected instanceof Object[]) {
                return objectArrayDeepEquals((Object[]) actual, (Object[]) expected);
            }
            if ((actual instanceof Integer || actual instanceof Long)
                    && (expected instanceof Integer || expected instanceof Long)) {
                return ((Number) actual).longValue() == ((Number) expected).longValue();
            }
            if (actual instanceof Double || expected instanceof Double) {
                return Math.abs(((Number) actual).doubleValue() - ((Number) expected).doubleValue()) < 1e-5;
            }
            if (actual instanceof Float || expected instanceof Float) {
                return Math.abs(((Number) actual).floatValue() - ((Number) expected).floatValue()) < 1e-5;
            }
            if (actual instanceof Character && expected instanceof String) {
                return expected.equals(String.valueOf(actual));
            }
            if (actual instanceof String && expected instanceof Character) {
                return actual.equals(String.valueOf(expected));
            }
            return Objects.equals(actual, expected);
        }

        static boolean arraysApproxEqual(double[] actual, double[] expected) {
            if (actual.length != expected.length) return false;
            for (int i = 0; i < actual.length; i++) {
                if (Math.abs(actual[i] - expected[i]) >= 1e-5) return false;
            }
            return true;
        }

        static boolean arrayObjectApproxEqual(double[] actual, Object[] expected) {
            if (actual.length != expected.length) return false;
            for (int i = 0; i < expected.length; i++) {
                if (Math.abs(actual[i] - ((Number) expected[i]).doubleValue()) >= 1e-5) return false;
            }
            return true;
        }

        static boolean objectArrayDeepEquals(Object[] actual, Object[] expected) {
            if (actual.length != expected.length) return false;
            for (int i = 0; i < expected.length; i++) {
                if (!deepEquals(actual[i], expected[i])) return false;
            }
            return true;
        }

        static boolean objectArrayIntArrayEquals(Object[] actual, int[] expected) {
            if (actual.length != expected.length) return false;
            for (int i = 0; i < expected.length; i++) {
                if (actual[i] == null || ((Number) actual[i]).intValue() != expected[i]) return false;
            }
            return true;
        }
        """
    ).strip()


def java_mock_grid_master_helpers() -> str:
    # GridMaster interface is defined in the problem's Solution.java (LeetCode style).
    return textwrap.dedent(
        """
        static class MockGridMaster implements GridMaster {
            final int[][] grid;
            int row;
            int col;
            final int targetRow;
            final int targetCol;
            static final int[][] DELTA = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
            static final char[] DIRS = {'U', 'D', 'L', 'R'};

            MockGridMaster(int[][] grid, int r1, int c1, int r2, int c2) {
                this.grid = grid;
                this.row = r1;
                this.col = c1;
                this.targetRow = r2;
                this.targetCol = c2;
            }

            int dirIndex(char direction) {
                for (int i = 0; i < DIRS.length; i++) {
                    if (DIRS[i] == direction) return i;
                }
                return -1;
            }

            public boolean canMove(char direction) {
                int idx = dirIndex(direction);
                int nr = row + DELTA[idx][0];
                int nc = col + DELTA[idx][1];
                if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length) return false;
                return grid[nr][nc] != 0;
            }

            public int move(char direction) {
                if (!canMove(direction)) return -1;
                int idx = dirIndex(direction);
                row += DELTA[idx][0];
                col += DELTA[idx][1];
                return grid[row][col];
            }

            public boolean isTarget() {
                return row == targetRow && col == targetCol;
            }
        }

        static int runFindShortestPath(Solution solution, int[][] grid, int r1, int c1, int r2, int c2) {
            return solution.findShortestPath(new MockGridMaster(grid, r1, c1, r2, c2));
        }
        """
    ).strip()


def java_mock_robot_helpers() -> str:
    return textwrap.dedent(
        """
        static class MockRobot implements Robot {
            final int[][] room;
            int row;
            int col;
            int direction = 0;
            final Set<String> cleaned = new HashSet<>();
            final int[][] directions = new int[4][2];

            MockRobot(int[][] room, int row, int col) {
                this.room = room;
                this.row = row;
                this.col = col;
                directions[0][0] = -1; directions[0][1] = 0;
                directions[1][0] = 0; directions[1][1] = 1;
                directions[2][0] = 1; directions[2][1] = 0;
                directions[3][0] = 0; directions[3][1] = -1;
            }

            public boolean move() {
                int nr = row + directions[direction][0];
                int nc = col + directions[direction][1];
                if (nr >= 0 && nr < room.length && nc >= 0 && nc < room[0].length && room[nr][nc] == 1) {
                    row = nr;
                    col = nc;
                    return true;
                }
                return false;
            }

            public void turnLeft() { direction = (direction + 3) % 4; }
            public void turnRight() { direction = (direction + 1) % 4; }
            public void clean() { cleaned.add(row + "," + col); }

            boolean allCleaned() {
                for (int r = 0; r < room.length; r++) {
                    for (int c = 0; c < room[r].length; c++) {
                        if (room[r][c] == 1 && !cleaned.contains(r + "," + c)) return false;
                    }
                }
                return true;
            }
        }

        static String runCleanRoom(Solution solution, int[][] room, int row, int col) {
            MockRobot robot = new MockRobot(room, row, col);
            solution.cleanRoom(robot);
            return robot.allCleaned() ? "Robot cleaned all rooms." : "Robot missed rooms.";
        }
        """
    ).strip()


def java_tree_node_helpers() -> str:
    return textwrap.dedent(
        """
        static TreeNode listToTree(Object[] values) {
            if (values == null || values.length == 0) return null;
            TreeNode root = new TreeNode(((Number) values[0]).intValue());
            Queue<TreeNode> queue = new LinkedList<>();
            queue.offer(root);
            int index = 1;
            while (!queue.isEmpty() && index < values.length) {
                TreeNode node = queue.poll();
                if (index < values.length) {
                    if (values[index] != null) {
                        node.left = new TreeNode(((Number) values[index]).intValue());
                        queue.offer(node.left);
                    }
                    index++;
                }
                if (index < values.length) {
                    if (values[index] != null) {
                        node.right = new TreeNode(((Number) values[index]).intValue());
                        queue.offer(node.right);
                    }
                    index++;
                }
            }
            return root;
        }

        static TreeNode listToTree(int[] values) {
            if (values == null || values.length == 0) return null;
            Object[] boxed = new Object[values.length];
            for (int i = 0; i < values.length; i++) boxed[i] = values[i];
            return listToTree(boxed);
        }

        static TreeNode findTreeNode(TreeNode root, int val) {
            if (root == null) return null;
            if (root.val == val) return root;
            TreeNode left = findTreeNode(root.left, val);
            return left != null ? left : findTreeNode(root.right, val);
        }

        static Object[] treeToList(TreeNode root) {
            if (root == null) return new Object[0];
            List<Object> result = new ArrayList<>();
            Queue<TreeNode> queue = new LinkedList<>();
            queue.offer(root);
            while (!queue.isEmpty()) {
                TreeNode node = queue.poll();
                if (node == null) {
                    result.add(null);
                    continue;
                }
                result.add(node.val);
                queue.offer(node.left);
                queue.offer(node.right);
            }
            while (!result.isEmpty() && result.get(result.size() - 1) == null) {
                result.remove(result.size() - 1);
            }
            return result.toArray();
        }
        """
    ).strip()


def java_parent_node_helpers() -> str:
    return textwrap.dedent(
        """
        static Node listToParentTree(Object[] values) {
            if (values == null || values.length == 0) return null;
            Node root = new Node(((Number) values[0]).intValue());
            Queue<Node> queue = new LinkedList<>();
            queue.offer(root);
            int index = 1;
            while (!queue.isEmpty() && index < values.length) {
                Node node = queue.poll();
                if (index < values.length) {
                    if (values[index] != null) {
                        node.left = new Node(((Number) values[index]).intValue());
                        node.left.parent = node;
                        queue.offer(node.left);
                    }
                    index++;
                }
                if (index < values.length) {
                    if (values[index] != null) {
                        node.right = new Node(((Number) values[index]).intValue());
                        node.right.parent = node;
                        queue.offer(node.right);
                    }
                    index++;
                }
            }
            return root;
        }

        static Node findParentNode(Node root, int val) {
            if (root == null) return null;
            if (root.val == val) return root;
            Node left = findParentNode(root.left, val);
            return left != null ? left : findParentNode(root.right, val);
        }

        static Object[] parentTreeToList(Node root) {
            if (root == null) return new Object[0];
            List<Object> result = new ArrayList<>();
            Queue<Node> queue = new LinkedList<>();
            queue.offer(root);
            while (!queue.isEmpty()) {
                Node node = queue.poll();
                if (node == null) {
                    result.add(null);
                    continue;
                }
                result.add(node.val);
                queue.offer(node.left);
                queue.offer(node.right);
            }
            while (!result.isEmpty() && result.get(result.size() - 1) == null) {
                result.remove(result.size() - 1);
            }
            return result.toArray();
        }
        """
    ).strip()


def java_tree_helpers(include_parent_node: bool = False, include_tree_node: bool = True) -> str:
    helpers = []
    if include_tree_node:
        helpers.append(java_tree_node_helpers())
    if include_parent_node:
        helpers.append(java_parent_node_helpers())
    return "\n\n".join(helpers)


def build_design_test_source(config: dict, cases_doc: dict, void_methods: set[str] | None = None) -> str:
    void_methods = void_methods or set()
    case_blocks = []
    for case_index, case in enumerate(cases_doc.get("cases", []), start=1):
        operations = case["operations"]
        arguments = case["arguments"]
        expected = case["expected"]
        class_name = operations[0]
        uniform_setup = ""
        uniform_sequence = case.get("randomUniformSequence")
        if uniform_sequence is not None:
            uniform_setup = f"Uniform.setSequence({java_literal(uniform_sequence)});"
        step_blocks = [uniform_setup, "Object instance = null;"] if uniform_setup else ["Object instance = null;"]

        for step_index, operation in enumerate(operations):
            call_args = arguments[step_index] if step_index < len(arguments) else []
            arg_exprs = [java_literal(arg) for arg in call_args]
            arg_list = ", ".join(arg_exprs)
            expected_expr = java_literal(expected[step_index])

            if step_index == 0:
                step_blocks.append(
                    f"instance = new {operation}({arg_list});"
                    f"\n                    Object actual{step_index} = null;"
                )
            elif operation in void_methods:
                step_blocks.append(
                    f"(({class_name}) instance).{operation}({arg_list});"
                    f"\n                    Object actual{step_index} = null;"
                )
            else:
                step_blocks.append(
                    f"Object actual{step_index} = (({class_name}) instance).{operation}({arg_list});"
                )

            step_blocks.append(
                textwrap.dedent(
                    f"""
                    if (deepEquals(actual{step_index}, {expected_expr})) {{
                        // step {step_index + 1} ok
                    }} else {{
                        System.out.println("  FAIL case {case_index} step {step_index + 1}: expected " + stringify({expected_expr}) + ", got " + stringify(actual{step_index}));
                        failed = true;
                    }}
                    """
                ).strip()
            )

        body = "\n                    ".join(step_blocks)
        case_blocks.append(
            textwrap.dedent(
                f"""
                {{
                    boolean failed = false;
                    {body}
                    if (!failed) {{
                        passed++;
                        System.out.println("  PASS case {case_index}");
                    }}
                }}
                """
            ).strip()
        )

    cases_joined = "\n        ".join(case_blocks) if case_blocks else 'System.out.println("  SKIP no test cases defined in tests/cases.json");'

    return textwrap.dedent(
        f"""
        import java.util.*;

        public class GeneratedTestRunner {{
            static class ListNode {{
                int val;
                ListNode next;
                ListNode(int val) {{ this.val = val; }}
            }}

            {java_deep_equals_helpers()}

            static boolean deepEquals(Object actual, Object expected) {{
                return valuesEqual(actual, expected)
                    || listLikeEquals(actual, expected);
            }}

            static boolean listLikeEquals(Object actual, Object expected) {{
                if (actual instanceof List<?>) {{
                    if (expected instanceof List<?>) return listDeepEquals((List<?>) actual, (List<?>) expected);
                    if (expected instanceof Object[]) return listArrayDeepEquals((List<?>) actual, (Object[]) expected);
                    if (expected instanceof int[]) return listIntArrayEquals((List<?>) actual, (int[]) expected);
                    if (expected instanceof boolean[]) return listBoolArrayEquals((List<?>) actual, (boolean[]) expected);
                }}
                return false;
            }}

            static boolean listArrayDeepEquals(List<?> actual, Object[] expected) {{
                if (actual.size() != expected.length) return false;
                for (int i = 0; i < expected.length; i++) {{
                    if (!valuesEqual(actual.get(i), expected[i])) return false;
                }}
                return true;
            }}

            static boolean listIntArrayEquals(List<?> actual, int[] expected) {{
                if (actual.size() != expected.length) return false;
                for (int i = 0; i < expected.length; i++) {{
                    if (!(actual.get(i) instanceof Number) || ((Number) actual.get(i)).intValue() != expected[i]) return false;
                }}
                return true;
            }}

            static boolean listBoolArrayEquals(List<?> actual, boolean[] expected) {{
                if (actual.size() != expected.length) return false;
                for (int i = 0; i < expected.length; i++) {{
                    if (!(actual.get(i) instanceof Boolean) || (Boolean) actual.get(i) != expected[i]) return false;
                }}
                return true;
            }}

            static boolean listDeepEquals(List<?> actual, List<?> expected) {{
                if (actual.size() != expected.size()) return false;
                for (int i = 0; i < actual.size(); i++) {{
                    if (!valuesEqual(actual.get(i), expected.get(i))) return false;
                }}
                return true;
            }}

            public static void main(String[] args) {{
                int passed = 0;
                int total = {len(cases_doc.get("cases", []))};
                System.out.println("Java design tests");
                {cases_joined}
                System.out.println("Result: " + passed + "/" + total + " passed");
                if (passed != total) System.exit(1);
            }}
        }}
        """
    )

def build_test_source(config: dict, cases_doc: dict, define_listnode: bool = True) -> str:
    method_name = config["method"]
    class_name = config.get("class", "Solution")
    param_order = config.get("paramOrder") or (list(cases_doc["cases"][0]["args"].keys()) if cases_doc.get("cases") else [])
    arg_types = config.get("types") or {}
    return_type = arg_types.get("return")
    uses_parent_node = False
    uses_lca_nodes = False
    uses_lca_pq = False
    uses_nearest_right = False

    case_blocks = []
    for index, case in enumerate(cases_doc.get("cases", []), start=1):
        args = case["args"]
        expected = case["expected"]
        nested_p = args.get("p")

        # 1650-style: p embeds {tree,p,q} and uses Node with parent pointers.
        if (
            method_name == "lowestCommonAncestor"
            and isinstance(nested_p, dict)
            and "tree" in nested_p
            and "p" in nested_p
            and "q" in nested_p
        ):
            uses_parent_node = True
            tree_expr = java_literal(nested_p["tree"])
            expected_expr = java_literal(expected)
            actual_expr = f"runParentLca(solution, {tree_expr}, {nested_p['p']}, {nested_p['q']})"
            solution_decl = f"{class_name} solution = new {class_name}();"
            case_blocks.append(
                textwrap.dedent(
                    f"""
                    {{
                        {solution_decl}
                        Object expected = {expected_expr};
                        Object actual = {actual_expr};
                        if (deepEquals(actual, expected)) {{
                            passed++;
                            System.out.println("  PASS case {index}");
                        }} else {{
                            System.out.println("  FAIL case {index}: expected " + stringify(expected) + ", got " + stringify(actual));
                        }}
                    }}
                    """
                ).strip()
            )
            continue

        # 1660: inject invalid right edge before calling correctBinaryTree(root).
        if method_name == "correctBinaryTree" and "fromNode" in args and "toNode" in args:
            expected_expr = java_literal(expected)
            actual_expr = (
                f"runCorrectBinaryTree(solution, {java_literal(args['root'])}, "
                f"{args['fromNode']}, {args['toNode']})"
            )
            solution_decl = f"{class_name} solution = new {class_name}();"
            case_blocks.append(
                textwrap.dedent(
                    f"""
                    {{
                        {solution_decl}
                        Object expected = {expected_expr};
                        Object actual = {actual_expr};
                        if (deepEquals(actual, expected)) {{
                            passed++;
                            System.out.println("  PASS case {index}");
                        }} else {{
                            System.out.println("  FAIL case {index}: expected " + stringify(expected) + ", got " + stringify(actual));
                        }}
                    }}
                    """
                ).strip()
            )
            continue

        # 1666: build Node tree with parent pointers, then flip.
        if method_name == "flipBinaryTree" and "leaf" in args:
            uses_parent_node = True
            expected_expr = java_literal(expected)
            actual_expr = f"runFlipBinaryTree(solution, {java_literal(args['root'])}, {args['leaf']})"
            solution_decl = f"{class_name} solution = new {class_name}();"
            case_blocks.append(
                textwrap.dedent(
                    f"""
                    {{
                        {solution_decl}
                        Object expected = {expected_expr};
                        Object actual = {actual_expr};
                        if (deepEquals(actual, expected)) {{
                            passed++;
                            System.out.println("  PASS case {index}");
                        }} else {{
                            System.out.println("  FAIL case {index}: expected " + stringify(expected) + ", got " + stringify(actual));
                        }}
                    }}
                    """
                ).strip()
            )
            continue

        # 1676: resolve node values to TreeNode[], compare returned node.val.
        if method_name == "lowestCommonAncestor" and "root" in args and "nodes" in args:
            uses_lca_nodes = True
            expected_expr = java_literal(expected)
            actual_expr = (
                f"runLcaNodes(solution, {java_literal(args['root'])}, {java_literal(args['nodes'])})"
            )
            solution_decl = f"{class_name} solution = new {class_name}();"
            case_blocks.append(
                textwrap.dedent(
                    f"""
                    {{
                        {solution_decl}
                        Object expected = {expected_expr};
                        Object actual = {actual_expr};
                        if (deepEquals(actual, expected)) {{
                            passed++;
                            System.out.println("  PASS case {index}");
                        }} else {{
                            System.out.println("  FAIL case {index}: expected " + stringify(expected) + ", got " + stringify(actual));
                        }}
                    }}
                    """
                ).strip()
            )
            continue

        # Standard LCA / nearest-right: resolve int node ids to TreeNode, compare .val.
        if (
            method_name == "lowestCommonAncestor"
            and "root" in args
            and "p" in args
            and "q" in args
            and not isinstance(args.get("p"), dict)
        ):
            uses_lca_pq = True
            expected_expr = java_literal(expected)
            actual_expr = (
                f"runLcaPq(solution, {java_literal(args['root'])}, "
                f"{java_literal(args['p'])}, {java_literal(args['q'])})"
            )
            solution_decl = f"{class_name} solution = new {class_name}();"
            case_blocks.append(
                textwrap.dedent(
                    f"""
                    {{
                        {solution_decl}
                        Object expected = {expected_expr};
                        Object actual = {actual_expr};
                        if (deepEquals(actual, expected)) {{
                            passed++;
                            System.out.println("  PASS case {index}");
                        }} else {{
                            System.out.println("  FAIL case {index}: expected " + stringify(expected) + ", got " + stringify(actual));
                        }}
                    }}
                    """
                ).strip()
            )
            continue

        if method_name == "findNearestRightNode" and "root" in args and "u" in args:
            uses_nearest_right = True
            expected_expr = java_literal(expected)
            actual_expr = (
                f"runFindNearestRightNode(solution, {java_literal(args['root'])}, "
                f"{java_literal(args['u'])})"
            )
            solution_decl = f"{class_name} solution = new {class_name}();"
            case_blocks.append(
                textwrap.dedent(
                    f"""
                    {{
                        {solution_decl}
                        Object expected = {expected_expr};
                        Object actual = {actual_expr};
                        if (deepEquals(actual, expected)) {{
                            passed++;
                            System.out.println("  PASS case {index}");
                        }} else {{
                            System.out.println("  FAIL case {index}: expected " + stringify(expected) + ", got " + stringify(actual));
                        }}
                    }}
                    """
                ).strip()
            )
            continue

        if method_name == "expTree" and class_name == "TreeBuilder":
            expected_expr = java_literal(expected)
            actual_expr = f"solution.expTree({java_literal(args['postfix'])}).evaluate()"
            solution_decl = f"{class_name} solution = new {class_name}();"
            case_blocks.append(
                textwrap.dedent(
                    f"""
                    {{
                        {solution_decl}
                        Object expected = {expected_expr};
                        Object actual = {actual_expr};
                        if (deepEquals(actual, expected)) {{
                            passed++;
                            System.out.println("  PASS case {index}");
                        }} else {{
                            System.out.println("  FAIL case {index}: expected " + stringify(expected) + ", got " + stringify(actual));
                        }}
                    }}
                    """
                ).strip()
            )
            continue

        arg_exprs = []
        if not (
            (method_name == "cleanRoom" and "room" in args)
            or (method_name == "findShortestPath" and "grid" in args)
        ):
            if class_name == "Codec" and ("url" in args or "longUrl" in args):
                pass
            else:
                for key in param_order:
                    value = args[key]
                    if arg_types.get(key) == "listnode":
                        arg_exprs.append(f"toListNode({java_literal(value)})")
                    elif arg_types.get(key) == "treenode":
                        arg_exprs.append(f"listToTree({java_literal(value)})")
                    else:
                        arg_exprs.append(java_literal(value))
        if return_type == "listnode":
            expected_expr = f"fromListNode(toListNode({java_literal(expected)}))"
            actual_expr = f"fromListNode(solution.{method_name}({', '.join(arg_exprs)}))"
        elif (
            class_name == "Codec"
            and ("url" in args or "longUrl" in args)
        ):
            long_url = args.get("url") or args.get("longUrl")
            expected_expr = java_literal(expected)
            actual_expr = f"codec.decode(codec.encode({java_literal(long_url)}))"
        elif return_type == "treenode":
            expected_expr = java_literal(expected)
            actual_expr = f"treeToList(solution.{method_name}({', '.join(arg_exprs)}))"
        elif return_type == "void" and "root" in args and arg_types.get("root") == "treenode":
            expected_expr = java_literal(expected)
            root_expr = f"listToTree({java_literal(args['root'])})"
            actual_expr = f"runVoidTreeMutation(solution, {root_expr})"
        elif method_name == "findShortestPath" and "grid" in args:
            expected_expr = java_literal(expected)
            actual_expr = (
                f"runFindShortestPath(solution, {java_literal(args['grid'])}, "
                f"{args['r1']}, {args['c1']}, {args['r2']}, {args['c2']})"
            )
        else:
            expected_expr = java_literal(expected)
            actual_expr = f"solution.{method_name}({', '.join(arg_exprs)})"

        if method_name == "guessNumber" and "pick" in args:
            pick = args["pick"]
            solution_decl = textwrap.dedent(
                f"""
                Solution solution = new Solution() {{
                    @Override
                    protected int guess(int num) {{
                        if (num > {pick}) return -1;
                        if (num < {pick}) return 1;
                        return 0;
                    }}
                }};
                """
            ).strip()
        elif method_name == "rand10" and "n" in args:
            sequence = case.get("rand7Sequence", [])
            count = args["n"]
            solution_decl = f"Rand7.setSequence({java_literal(sequence)});\n                    Solution solution = new Solution();"
            actual_expr = f"collectRand10(solution, {count})"
        elif method_name == "cleanRoom" and "room" in args:
            room = java_literal(args["room"])
            row = args["row"]
            col = args["col"]
            solution_decl = f"{class_name} solution = new {class_name}();"
            actual_expr = f"runCleanRoom(solution, {room}, {row}, {col})"
        elif class_name == "Codec" and ("url" in args or "longUrl" in args):
            solution_decl = f"{class_name} codec = new {class_name}();"
        elif return_type == "void" and "root" in args and arg_types.get("root") == "treenode":
            solution_decl = f"{class_name} solution = new {class_name}();"
        else:
            solution_decl = f"{class_name} solution = new {class_name}();"

        case_blocks.append(
            textwrap.dedent(
                f"""
                {{
                    {solution_decl}
                    Object expected = {expected_expr};
                    Object actual = {actual_expr};
                    if (deepEquals(actual, expected)) {{
                        passed++;
                        System.out.println("  PASS case {index}");
                    }} else {{
                        System.out.println("  FAIL case {index}: expected " + stringify(expected) + ", got " + stringify(actual));
                    }}
                }}
                """
            ).strip()
        )

    cases_joined = "\n        ".join(case_blocks) if case_blocks else 'System.out.println("  SKIP no test cases defined in tests/cases.json");'
    mock_robot_helpers = java_mock_robot_helpers() if method_name == "cleanRoom" else ""
    mock_grid_helpers = java_mock_grid_master_helpers() if method_name == "findShortestPath" else ""
    rand10_helpers = (
        textwrap.dedent(
            """
            static int[] collectRand10(Solution solution, int count) {
                int[] values = new int[count];
                for (int i = 0; i < count; i++) {
                    values[i] = solution.rand10();
                }
                return values;
            }
            """
        ).strip()
        if method_name == "rand10"
        else ""
    )
    needs_tree_node = (
        (
            return_type == "treenode"
            or any(arg_types.get(key) == "treenode" for key in param_order)
            or method_name == "correctBinaryTree"
            or uses_lca_nodes
            or uses_lca_pq
            or uses_nearest_right
            or method_name == "isEvenOddTree"
        )
        and method_name != "flipBinaryTree"
    )
    needs_parent = uses_parent_node or method_name == "flipBinaryTree"
    if needs_tree_node or needs_parent:
        tree_helpers = java_tree_helpers(
            include_parent_node=needs_parent,
            include_tree_node=needs_tree_node,
        )
    else:
        tree_helpers = ""
    special_helpers = []
    if method_name == "correctBinaryTree":
        special_helpers.append(
            textwrap.dedent(
                f"""
                static Object[] toObjectArray(int[] values) {{
                    Object[] out = new Object[values.length];
                    for (int i = 0; i < values.length; i++) out[i] = values[i];
                    return out;
                }}

                static Object[] runCorrectBinaryTree({class_name} solution, Object[] values, int fromNode, int toNode) {{
                    TreeNode root = listToTree(values);
                    TreeNode from = findTreeNode(root, fromNode);
                    TreeNode to = findTreeNode(root, toNode);
                    from.right = to;
                    return treeToList(solution.correctBinaryTree(root));
                }}

                static Object[] runCorrectBinaryTree({class_name} solution, int[] values, int fromNode, int toNode) {{
                    return runCorrectBinaryTree(solution, toObjectArray(values), fromNode, toNode);
                }}
                """
            ).strip()
        )
    if method_name == "flipBinaryTree":
        special_helpers.append(
            textwrap.dedent(
                f"""
                static Object[] runFlipBinaryTree({class_name} solution, Object[] values, int leafVal) {{
                    Node root = listToParentTree(values);
                    Node leaf = findParentNode(root, leafVal);
                    return parentTreeToList(solution.flipBinaryTree(root, leaf));
                }}

                static Object[] runFlipBinaryTree({class_name} solution, int[] values, int leafVal) {{
                    Object[] boxed = new Object[values.length];
                    for (int i = 0; i < values.length; i++) boxed[i] = values[i];
                    return runFlipBinaryTree(solution, boxed, leafVal);
                }}
                """
            ).strip()
        )
    if uses_parent_node and method_name == "lowestCommonAncestor":
        special_helpers.append(
            textwrap.dedent(
                f"""
                static Integer runParentLca({class_name} solution, Object[] values, int pVal, int qVal) {{
                    Node root = listToParentTree(values);
                    Node p = findParentNode(root, pVal);
                    Node q = findParentNode(root, qVal);
                    Node got = solution.lowestCommonAncestor(p, q);
                    return got == null ? null : got.val;
                }}
                """
            ).strip()
        )
    if uses_lca_nodes:
        special_helpers.append(
            textwrap.dedent(
                f"""
                static Integer runLcaNodes({class_name} solution, Object[] values, int[] nodeVals) {{
                    TreeNode root = listToTree(values);
                    TreeNode[] nodes = new TreeNode[nodeVals.length];
                    for (int i = 0; i < nodeVals.length; i++) {{
                        nodes[i] = findTreeNode(root, nodeVals[i]);
                    }}
                    TreeNode got = solution.lowestCommonAncestor(root, nodes);
                    return got == null ? null : got.val;
                }}
                """
            ).strip()
        )
    if uses_lca_pq:
        special_helpers.append(
            textwrap.dedent(
                f"""
                static Integer runLcaPq({class_name} solution, Object[] values, int pVal, int qVal) {{
                    TreeNode root = listToTree(values);
                    TreeNode got = solution.lowestCommonAncestor(
                        root, findTreeNode(root, pVal), findTreeNode(root, qVal));
                    return got == null ? null : got.val;
                }}
                static Integer runLcaPq({class_name} solution, int[] values, int pVal, int qVal) {{
                    TreeNode root = listToTree(values);
                    TreeNode got = solution.lowestCommonAncestor(
                        root, findTreeNode(root, pVal), findTreeNode(root, qVal));
                    return got == null ? null : got.val;
                }}
                """
            ).strip()
        )
    if uses_nearest_right:
        special_helpers.append(
            textwrap.dedent(
                f"""
                static Integer runFindNearestRightNode({class_name} solution, Object[] values, int uVal) {{
                    TreeNode root = listToTree(values);
                    TreeNode got = solution.findNearestRightNode(root, findTreeNode(root, uVal));
                    return got == null ? null : got.val;
                }}
                static Integer runFindNearestRightNode({class_name} solution, int[] values, int uVal) {{
                    TreeNode root = listToTree(values);
                    TreeNode got = solution.findNearestRightNode(root, findTreeNode(root, uVal));
                    return got == null ? null : got.val;
                }}
                """
            ).strip()
        )
    special_helpers_src = "\n\n".join(special_helpers)
    void_tree_helper = ""
    if return_type == "void" and arg_types.get("root") == "treenode":
        void_tree_helper = textwrap.dedent(
            f"""
            static Object[] runVoidTreeMutation({class_name} solution, TreeNode root) {{
                solution.{method_name}(root);
                return treeToList(root);
            }}
            """
        ).strip()

    listnode_decl = (
        textwrap.dedent(
            """
            class ListNode {
                int val;
                ListNode next;
                ListNode(int val) { this.val = val; }
            }
            """
        ).strip()
        if define_listnode
        else ""
    )

    return textwrap.dedent(
        f"""
        import java.util.*;

        {listnode_decl}

        public class GeneratedTestRunner {{
            static ListNode toListNode(int[] values) {{
                if (values == null || values.length == 0) return null;
                ListNode head = new ListNode(values[0]);
                ListNode current = head;
                for (int i = 1; i < values.length; i++) {{
                    current.next = new ListNode(values[i]);
                    current = current.next;
                }}
                return head;
            }}

            static int[] fromListNode(ListNode node) {{
                List<Integer> values = new ArrayList<>();
                while (node != null) {{
                    values.add(node.val);
                    node = node.next;
                }}
                return values.stream().mapToInt(Integer::intValue).toArray();
            }}

            {java_deep_equals_helpers()}

            static boolean deepEquals(Object actual, Object expected) {{
                if (actual instanceof List<?> && expected instanceof List<?>) {{
                    return listDeepEquals((List<?>) actual, (List<?>) expected);
                }}
                if (actual instanceof List<?> && expected instanceof Object[]) {{
                    return listArrayDeepEquals((List<?>) actual, (Object[]) expected);
                }}
                if (actual instanceof List<?> && expected instanceof int[]) {{
                    return listIntArrayEquals((List<?>) actual, (int[]) expected);
                }}
                if (actual instanceof List<?> && expected instanceof boolean[]) {{
                    return listBoolArrayEquals((List<?>) actual, (boolean[]) expected);
                }}
                return valuesEqual(actual, expected);
            }}

            static boolean listArrayDeepEquals(List<?> actual, Object[] expected) {{
                if (actual.size() != expected.length) return false;
                for (int i = 0; i < expected.length; i++) {{
                    if (!valuesEqual(actual.get(i), expected[i])) return false;
                }}
                return true;
            }}

            static boolean listIntArrayEquals(List<?> actual, int[] expected) {{
                if (actual.size() != expected.length) return false;
                for (int i = 0; i < expected.length; i++) {{
                    if (!(actual.get(i) instanceof Number) || ((Number) actual.get(i)).intValue() != expected[i]) return false;
                }}
                return true;
            }}

            static boolean listBoolArrayEquals(List<?> actual, boolean[] expected) {{
                if (actual.size() != expected.length) return false;
                for (int i = 0; i < expected.length; i++) {{
                    if (!(actual.get(i) instanceof Boolean) || (Boolean) actual.get(i) != expected[i]) return false;
                }}
                return true;
            }}

            static boolean listDeepEquals(List<?> actual, List<?> expected) {{
                if (actual.size() != expected.size()) return false;
                for (int i = 0; i < actual.size(); i++) {{
                    if (!valuesEqual(actual.get(i), expected.get(i))) return false;
                }}
                return true;
            }}

            {rand10_helpers}

            {mock_robot_helpers}

            {mock_grid_helpers}

            {tree_helpers}

            {special_helpers_src}

            {void_tree_helper}

            public static void main(String[] args) {{
                int passed = 0;
                int total = {len(cases_doc.get("cases", []))};
                System.out.println("Java tests: {method_name}()");
                {cases_joined}
                System.out.println("Result: " + passed + "/" + total + " passed");
                if (passed != total) System.exit(1);
            }}
        }}
        """
    )



def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: run_tests.py <problem_dir>")
        return 2

    problem_dir = Path(sys.argv[1]).resolve()
    config, cases_doc = load_problem_tests(problem_dir)

    java_files = list(problem_dir.glob("*.java"))
    can_run, exit_code, message = pre_run_check(
        "java",
        config,
        cases_doc,
        has_solution_file=bool(java_files),
        toolchain_available=shutil.which("javac") is not None and shutil.which("java") is not None,
    )
    if not can_run:
        print(f"Java tests: {problem_dir.name}")
        print_skip(message)
        return exit_code

    is_design = uses_design_cases(cases_doc) or config.get("kind") == "design"
    label = "Java design tests" if is_design else f"Java tests: {problem_dir.name} :: {config.get('method', '?')}()"
    print(label)

    import tempfile

    temp_dir = Path(tempfile.mkdtemp())
    try:
        for java_file in problem_dir.glob("*.java"):
            text = java_file.read_text(encoding="utf-8-sig")
            (temp_dir / java_file.name).write_text(text, encoding="utf-8")
        solution_defines_listnode = any(
            "class ListNode" in f.read_text(encoding="utf-8-sig")
            for f in problem_dir.glob("*.java")
        )
        import re

        void_methods = {
            match.group(1)
            for f in problem_dir.glob("*.java")
            for match in re.finditer(r"\bvoid\s+(\w+)\s*\(", f.read_text(encoding="utf-8-sig"))
        }
        source = (
            build_design_test_source(config, cases_doc, void_methods)
            if is_design
            else build_test_source(config, cases_doc, define_listnode=not solution_defines_listnode)
        )
        (temp_dir / "GeneratedTestRunner.java").write_text(source, encoding="utf-8")
        java_sources = list(temp_dir.glob("*.java"))
        subprocess.check_call(["javac", *[str(path) for path in java_sources]], cwd=temp_dir)
        subprocess.check_call(["java", "-cp", str(temp_dir), "GeneratedTestRunner"], cwd=temp_dir)
        return 0
    except subprocess.CalledProcessError:
        return 1
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
