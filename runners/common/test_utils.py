#!/usr/bin/env python3
"""Shared test utilities for LeetCode solution runners."""

from __future__ import annotations

import json
import re
import threading
from io import StringIO
from pathlib import Path
from typing import Any


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class ParentNode:
    def __init__(
        self,
        val: int = 0,
        left: "ParentNode | None" = None,
        right: "ParentNode | None" = None,
        parent: "ParentNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class NextNode:
    def __init__(
        self,
        val: int = 0,
        left: "NextNode | None" = None,
        right: "NextNode | None" = None,
        next: "NextNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class GraphNode:
    def __init__(self, val: int = 0, neighbors: list["GraphNode"] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class RandomListNode:
    def __init__(
        self,
        val: int = 0,
        next: "RandomListNode | None" = None,
        random: "RandomListNode | None" = None,
    ):
        self.val = val
        self.next = next
        self.random = random


class NestedInteger:
    def __init__(self, value: int | None = None):
        self._integer = value
        self._list: list["NestedInteger"] = []

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int:
        return self._integer if self._integer is not None else 0

    def getList(self) -> list["NestedInteger"]:
        return self._list


def json_to_nested_integer(value: Any) -> NestedInteger:
    if isinstance(value, int):
        return NestedInteger(value)
    item = NestedInteger()
    item._list = [json_to_nested_integer(entry) for entry in value]
    return item


def json_to_nested_list(values: list[Any]) -> list[NestedInteger]:
    return [json_to_nested_integer(value) for value in values]


def nested_integer_to_value(item: NestedInteger) -> int | list[Any]:
    if item.isInteger():
        return item.getInteger()
    return [nested_integer_to_value(entry) for entry in item.getList()]


class NaryNode:
    def __init__(self, val: int | None = None, children: list["NaryNode"] | None = None):
        self.val = val
        self.children = children if children is not None else []


class QuadNode:
    def __init__(
        self,
        val: bool = False,
        isLeaf: bool = False,
        topLeft: "QuadNode | None" = None,
        topRight: "QuadNode | None" = None,
        bottomLeft: "QuadNode | None" = None,
        bottomRight: "QuadNode | None" = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class MultilevelNode:
    def __init__(
        self,
        val: int = 0,
        prev: "MultilevelNode | None" = None,
        next: "MultilevelNode | None" = None,
        child: "MultilevelNode | None" = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def list_to_nary(values: list[Any]) -> NaryNode | None:
    if not values:
        return None
    root = NaryNode(values[0], [])
    queue: list[NaryNode] = [root]
    # Format: [root, null, child-group, null, child-group, ...]
    index = 2 if len(values) > 1 else 1
    while queue and index < len(values):
        node = queue.pop(0)
        while index < len(values) and values[index] is not None:
            child = NaryNode(values[index], [])
            node.children.append(child)
            queue.append(child)
            index += 1
        index += 1  # skip the null ending this node's children
    return root


def nary_to_list(root: NaryNode | None) -> list[Any]:
    if root is None:
        return []
    result: list[Any] = [root.val, None]
    queue: list[NaryNode] = [root]
    while queue:
        node = queue.pop(0)
        for child in node.children:
            result.append(child.val)
            queue.append(child)
        result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def list_to_quad(values: list[Any]) -> QuadNode | None:
    if not values:
        return None

    def parse(data: Any) -> QuadNode | None:
        if data is None:
            return None
        return QuadNode(bool(data[1]), bool(data[0]))

    root = parse(values[0])
    if root is None:
        return None

    queue: list[QuadNode | None] = [root]
    index = 1
    while queue and index < len(values):
        node = queue.pop(0)
        if node is None:
            continue
        children: list[QuadNode | None] = []
        for _ in range(4):
            if index < len(values):
                child = parse(values[index])
                index += 1
            else:
                child = None
            children.append(child)
            queue.append(child)
        if not node.isLeaf:
            node.topLeft, node.topRight, node.bottomLeft, node.bottomRight = children
    return root


def quad_tree_to_list(root: QuadNode | None) -> list[Any]:
    if root is None:
        return []
    result: list[Any] = []
    queue: list[QuadNode | None] = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append([int(node.isLeaf), int(node.val)])
        if node.isLeaf:
            queue.extend([None, None, None, None])
        else:
            queue.extend([node.topLeft, node.topRight, node.bottomLeft, node.bottomRight])
    while result and result[-1] is None:
        result.pop()
    return result


def nary_trees_equal(left: Any, right: Any) -> bool:
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val != right.val or len(left.children) != len(right.children):
        return False
    return all(nary_trees_equal(a, b) for a, b in zip(left.children, right.children))


def split_multilevel_rows(values: list[Any]) -> list[list[int]]:
    rows: list[list[int]] = []
    index = 0
    length = len(values)
    while index < length:
        row: list[int] = []
        while index < length and values[index] is not None:
            row.append(index)
            index += 1
        if row:
            rows.append(row)
        if index < length and values[index] is None:
            index += 1
        while index < length and values[index] is None:
            index += 1
    return rows


def list_to_multilevel(values: list[Any]) -> MultilevelNode | None:
    if not values:
        return None
    nodes: dict[int, MultilevelNode] = {}
    for index, value in enumerate(values):
        if value is not None:
            nodes[index] = MultilevelNode(value)
    rows = split_multilevel_rows(values)
    for row in rows:
        for position, node_index in enumerate(row):
            node = nodes[node_index]
            if position > 0:
                previous_index = row[position - 1]
                node.prev = nodes[previous_index]
                nodes[previous_index].next = node
    for row_index in range(len(rows) - 1):
        parent_row = rows[row_index]
        child_row = rows[row_index + 1]
        padding = child_row[0] - parent_row[-1] - 2
        if padding < 0:
            padding = 0
        if padding < len(parent_row):
            nodes[parent_row[padding]].child = nodes[child_row[0]]
    return nodes[rows[0][0]]


def multilevel_to_list(head: MultilevelNode | None) -> list[int]:
    result: list[int] = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def doubly_tree_node_to_list(head: TreeNode | None) -> list[int]:
    if head is None:
        return []
    result: list[int] = []
    node = head
    start = head
    while True:
        result.append(node.val)
        if node.right is None or node.right is start:
            break
        node = node.right
    return result


def load_problem_tests(problem_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    tests_dir = problem_dir / "tests"
    config = json.loads((tests_dir / "config.json").read_text(encoding="utf-8-sig"))
    cases_doc = json.loads((tests_dir / "cases.json").read_text(encoding="utf-8-sig"))
    return config, cases_doc


def list_to_listnode(values: list[int] | None) -> ListNode | None:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def list_to_cyclelist(values: list[int] | None, pos: int = -1) -> ListNode | None:
    if not values:
        return None
    nodes = [ListNode(value) for value in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]
    return nodes[0]


def listnode_to_list(node: ListNode | None) -> list[int]:
    result: list[int] = []
    seen: set[int] = set()
    while node and id(node) not in seen:
        seen.add(id(node))
        result.append(node.val)
        node = node.next
    return result


def cycleentry_to_string(node: ListNode | None, head: ListNode | None) -> str:
    if node is None:
        return "no cycle"
    index = 0
    current = head
    seen: set[int] = set()
    while current and id(current) not in seen:
        if current is node:
            return f"tail connects to node index {index}"
        seen.add(id(current))
        current = current.next
        index += 1
    return "no cycle"


def build_intersection_lists(args: dict[str, Any]) -> tuple[ListNode | None, ListNode | None]:
    list_a = args.get("listA") or []
    list_b = args.get("listB") or []
    skip_a = int(args.get("skipA", 0))
    skip_b = int(args.get("skipB", 0))
    intersect_val = int(args.get("intersectVal", 0))

    if not list_a and not list_b:
        return None, None

    nodes_a = [ListNode(value) for value in list_a]
    for i in range(len(nodes_a) - 1):
        nodes_a[i].next = nodes_a[i + 1]

    if intersect_val == 0 or skip_a >= len(nodes_a):
        nodes_b = [ListNode(value) for value in list_b]
        for i in range(len(nodes_b) - 1):
            nodes_b[i].next = nodes_b[i + 1]
        return (nodes_a[0] if nodes_a else None), (nodes_b[0] if nodes_b else None)

    nodes_b = [ListNode(value) for value in list_b[:skip_b]]
    for i in range(len(nodes_b) - 1):
        nodes_b[i].next = nodes_b[i + 1]
    if nodes_b:
        nodes_b[-1].next = nodes_a[skip_a]
    else:
        nodes_b = [nodes_a[skip_a]]
    return nodes_a[0], nodes_b[0]


def intersectnode_to_string(node: ListNode | None) -> str:
    if node is None:
        return "No intersection"
    return f"Intersected at '{node.val}'"


def find_tree_node(root: TreeNode | None, val: int) -> TreeNode | None:
    if not root:
        return None
    if root.val == val:
        return root
    left = find_tree_node(root.left, val)
    if left:
        return left
    return find_tree_node(root.right, val)


def list_to_parent_tree(values: list[Any]) -> ParentNode | None:
    if not values:
        return None
    root = ParentNode(values[0])
    queue: list[ParentNode] = [root]
    index = 1
    while queue and index < len(values):
        node = queue.pop(0)
        if index < len(values):
            if values[index] is not None:
                node.left = ParentNode(values[index])
                node.left.parent = node
                queue.append(node.left)
            index += 1
        if index < len(values):
            if values[index] is not None:
                node.right = ParentNode(values[index])
                node.right.parent = node
                queue.append(node.right)
            index += 1
    return root


def find_parent_node(root: ParentNode | None, val: int) -> ParentNode | None:
    if not root:
        return None
    if root.val == val:
        return root
    left = find_parent_node(root.left, val)
    if left:
        return left
    return find_parent_node(root.right, val)


def find_list_node(head: ListNode | None, val: int) -> ListNode | None:
    while head:
        if head.val == val:
            return head
        head = head.next
    return None


def list_to_tree(values: list[Any]) -> TreeNode | None:
    if not values:
        return None
    root = TreeNode(values[0])
    queue: list[TreeNode] = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root


def tree_to_list(root: TreeNode | None) -> list[Any]:
    if root is None:
        return []
    result: list[Any] = []
    queue: list[TreeNode | None] = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def list_to_nextnode(values: list[Any]) -> NextNode | None:
    if not values:
        return None
    root = NextNode(values[0])
    queue: list[NextNode] = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = NextNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = NextNode(values[i])
                queue.append(node.right)
            i += 1
    return root


def nextnode_to_serialized(root: NextNode | None) -> Any:
    if root is None:
        return []
    parts: list[str] = []
    level: NextNode | None = root
    while level:
        current: NextNode | None = level
        while current:
            parts.append(str(current.val))
            current = current.next
        parts.append("#")
        current = level
        next_level = None
        while current:
            if current.left:
                next_level = current.left
                break
            if current.right:
                next_level = current.right
                break
            current = current.next
        level = next_level
    return "[" + ",".join(parts) + "]"


def list_to_graph(adj_list: list[Any] | None) -> GraphNode | None:
    if not adj_list:
        return None
    nodes = [GraphNode(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]


def graph_to_list(node: GraphNode | None) -> list[Any]:
    if node is None:
        return []
    ordered: list[GraphNode] = []
    index: dict[int, int] = {}
    queue = [node]
    index[id(node)] = 0
    ordered.append(node)
    while queue:
        current = queue.pop(0)
        for neighbor in current.neighbors:
            if id(neighbor) not in index:
                index[id(neighbor)] = len(ordered)
                ordered.append(neighbor)
                queue.append(neighbor)
    ordered.sort(key=lambda item: item.val)
    result: list[list[int]] = [[] for _ in ordered]
    val_to_pos = {item.val: i for i, item in enumerate(ordered)}
    for item in ordered:
        result[val_to_pos[item.val]] = [neighbor.val for neighbor in item.neighbors]
    return result


def list_to_randomlist(pairs: list[Any] | None) -> RandomListNode | None:
    if not pairs:
        return None
    nodes = [RandomListNode(pair[0]) for pair in pairs]
    for i, pair in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if pair[1] is not None:
            nodes[i].random = nodes[pair[1]]
    return nodes[0]


def randomlist_to_list(head: RandomListNode | None) -> list[Any]:
    if head is None:
        return []
    nodes: list[RandomListNode] = []
    index: dict[int, int] = {}
    current: RandomListNode | None = head
    while current:
        index[id(current)] = len(nodes)
        nodes.append(current)
        current = current.next
    result: list[list[Any]] = []
    for node in nodes:
        random_index = index[id(node.random)] if node.random is not None else None
        result.append([node.val, random_index])
    return result


class RandomBinaryNode:
    """Binary tree node with a random pointer (problem 1485)."""

    def __init__(
        self,
        val: int = 0,
        left: "RandomBinaryNode | None" = None,
        right: "RandomBinaryNode | None" = None,
        random: "RandomBinaryNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


def list_to_random_binary(data: list[Any] | None) -> RandomBinaryNode | None:
    if not data:
        return None
    nodes: list[RandomBinaryNode | None] = [
        None if item is None else RandomBinaryNode(item[0]) for item in data
    ]
    for i, item in enumerate(data):
        if item is not None and item[1] is not None:
            nodes[i].random = nodes[item[1]]
    from collections import deque

    root = nodes[0]
    if root is None:
        return None
    queue: deque[RandomBinaryNode] = deque([root])
    i = 1
    while queue and i < len(nodes):
        current = queue.popleft()
        if i < len(nodes):
            current.left = nodes[i]
            if nodes[i] is not None:
                queue.append(nodes[i])
            i += 1
        if i < len(nodes):
            current.right = nodes[i]
            if nodes[i] is not None:
                queue.append(nodes[i])
            i += 1
    return root


def random_binary_to_list(root: RandomBinaryNode | None) -> list[Any]:
    if root is None:
        return []
    from collections import deque

    nodes: list[RandomBinaryNode | None] = []
    queue: deque[RandomBinaryNode | None] = deque([root])
    while queue:
        node = queue.popleft()
        nodes.append(node)
        if node is not None:
            queue.append(node.left)
            queue.append(node.right)
    while nodes and nodes[-1] is None:
        nodes.pop()
    index = {id(node): i for i, node in enumerate(nodes) if node is not None}
    result: list[Any] = []
    for node in nodes:
        if node is None:
            result.append(None)
        else:
            random_index = index[id(node.random)] if node.random is not None else None
            result.append([node.val, random_index])
    return result


class BinaryMatrix:
    """Local adapter for LeetCode's read-only BinaryMatrix API."""

    def __init__(self, mat: list[list[int]]):
        self._mat = mat

    def get(self, row: int, col: int) -> int:
        return self._mat[row][col]

    def dimensions(self) -> list[int]:
        return [len(self._mat), len(self._mat[0]) if self._mat else 0]


def convert_arg(value: Any, type_name: str | None) -> Any:
    if type_name == "binarymatrix":
        return BinaryMatrix(value)
    if type_name == "listnode":
        return list_to_listnode(value)
    if type_name == "listnode[]":
        return [list_to_listnode(item) if item else None for item in value]
    if type_name == "treenode":
        return list_to_tree(value)
    if type_name == "nextnode":
        return list_to_nextnode(value)
    if type_name == "graphnode":
        return list_to_graph(value)
    if type_name == "randomlistnode":
        return list_to_randomlist(value)
    if type_name == "randombinarynode":
        return list_to_random_binary(value)
    if type_name == "nestedinteger[]":
        return json_to_nested_list(value)
    if type_name == "narynode":
        return list_to_nary(value)
    if type_name == "quadnode":
        return list_to_quad(value)
    if type_name == "multilevelnode":
        return list_to_multilevel(value)
    return value


def parse_inplace_expected(expected: str) -> tuple[int, list[Any]] | None:
    match = re.match(r"(\d+),\s*(nums|chars)\s*=\s*\[(.*)\]", expected.strip())
    if not match:
        return None
    count = int(match.group(1))
    field = match.group(2)
    raw = match.group(3)
    if field == "chars":
        prefix = [
            token.strip().strip('"').strip("'")
            for token in re.findall(r'"[^"]*"|\'[^\']*\'|[^,\s]+', raw)
            if token.strip()
        ]
        return count, prefix
    prefix = [
        int(token.strip())
        for token in raw.split(",")
        if token.strip() and token.strip() != "_"
    ]
    return count, prefix


def is_inplace_expected(expected: Any) -> bool:
    return isinstance(expected, str) and (
        ", nums = [" in expected or ", chars = [" in expected
    )


def void_mutation_result(keys: list[str], values: list[Any]) -> Any:
    if "nums" in keys:
        return values[keys.index("nums")]
    if "nums1" in keys:
        return values[keys.index("nums1")]
    if "arr" in keys:
        return values[keys.index("arr")]
    if "board" in keys:
        return values[keys.index("board")]
    if "rooms" in keys:
        return values[keys.index("rooms")]
    if "matrix" in keys:
        return values[keys.index("matrix")]
    if "s" in keys:
        return values[keys.index("s")]
    if "root" in keys:
        return tree_to_list(values[keys.index("root")])
    if "head" in keys:
        return listnode_to_list(values[keys.index("head")])
    return None

def convert_result(value: Any, type_name: str | None) -> Any:
    if type_name == "listnode":
        return listnode_to_list(value)
    if type_name == "listnode[]":
        if value is None:
            return []
        return [listnode_to_list(item) for item in value]
    if type_name == "treenode":
        return tree_to_list(value)
    if type_name == "treenode[]":
        if value is None:
            return []
        return [tree_to_list(item) for item in value]
    if type_name == "nextnode":
        return nextnode_to_serialized(value)
    if type_name == "graphnode":
        return graph_to_list(value)
    if type_name == "randomlistnode":
        return randomlist_to_list(value)
    if type_name == "randombinarynode":
        return random_binary_to_list(value)
    if type_name == "nestedinteger":
        return nested_integer_to_value(value)
    if type_name == "narynode":
        return nary_to_list(value)
    if type_name == "quadnode":
        return quad_tree_to_list(value)
    if type_name == "multilevelnode":
        return multilevel_to_list(value)
    if type_name == "doublytreenode":
        return doubly_tree_node_to_list(value)
    return value


def deep_equal(actual: Any, expected: Any) -> bool:
    if isinstance(actual, list) and isinstance(expected, list):
        if len(actual) != len(expected):
            return False
        return all(deep_equal(a, e) for a, e in zip(actual, expected))
    if isinstance(actual, float) or isinstance(expected, float):
        return abs(float(actual) - float(expected)) < 1e-5
    return actual == expected


def trees_equal_any_order(actual: list[Any], expected: list[Any]) -> bool:
    return sorted(actual, key=lambda x: str(x)) == sorted(expected, key=lambda x: str(x))


def is_design_case(case: dict[str, Any]) -> bool:
    return case.get("kind") == "design"


def uses_design_cases(cases_doc: dict[str, Any]) -> bool:
    return any(is_design_case(case) for case in cases_doc.get("cases", []))


def _design_call_args(raw_args: Any) -> list[Any]:
    if raw_args is None:
        return []
    if isinstance(raw_args, list):
        return raw_args
    return [raw_args]


class ListIterator:
    def __init__(self, values: list[Any]) -> None:
        self.values = values
        self.index = 0

    def next(self) -> Any:
        value = self.values[self.index]
        self.index += 1
        return value

    def hasNext(self) -> bool:
        return self.index < len(self.values)


def run_design_case(module: Any, case: dict[str, Any]) -> tuple[bool, list[Any], list[Any]]:
    operations = case["operations"]
    arguments = case["arguments"]
    expected = case["expected"]
    instance = None
    actual_outputs: list[Any] = []

    uniform_sequence = case.get("randomUniformSequence")
    if uniform_sequence is not None:
        uniform_iter = iter(uniform_sequence)

        def mock_uniform(_a: float, _b: float) -> float:
            return next(uniform_iter)

        if hasattr(module, "set_uniform"):
            module.set_uniform(mock_uniform)
        else:
            module.uniform = mock_uniform

    for index, operation in enumerate(operations):
        call_args = _design_call_args(arguments[index] if index < len(arguments) else [])
        if index == 0:
            cls = getattr(module, operation)
            if operation == "BSTIterator" and call_args and isinstance(call_args[0], list):
                call_args = [list_to_tree(call_args[0])]
            if operation == "PeekingIterator" and call_args and isinstance(call_args[0], list):
                call_args = [ListIterator(call_args[0])]
            if operation == "NestedIterator" and call_args and isinstance(call_args[0], list):
                call_args = [json_to_nested_list(call_args[0])]
            if operation == "CBTInserter" and call_args and isinstance(call_args[0], list):
                call_args = [list_to_tree(call_args[0])]
            if operation == "FindElements" and call_args and isinstance(call_args[0], list):
                call_args = [list_to_tree(call_args[0])]
            instance = cls(*call_args) if call_args else cls()
            result = None
        else:
            if instance is None:
                raise RuntimeError(f"Design case missing constructor before operation {operation!r}")
            method = getattr(instance, operation)
            result = method(*call_args) if call_args else method()
            if operation == "get_root":
                result = tree_to_list(result)

        actual_outputs.append(result)
        if not deep_equal(result, expected[index]):
            return False, actual_outputs, expected

    return True, actual_outputs, expected


def run_design_cases(module: Any, cases_doc: dict[str, Any]) -> tuple[int, int]:
    passed = 0
    total = len(cases_doc.get("cases", []))

    for index, case in enumerate(cases_doc.get("cases", []), start=1):
        if not is_design_case(case):
            print(f"  SKIP case {index}: expected kind=design")
            continue

        try:
            ok, actual_outputs, expected = run_design_case(module, case)
        except Exception as exc:
            print(f"  FAIL case {index}: {exc}")
            continue

        if ok:
            passed += 1
            print(f"  PASS case {index}")
        else:
            step = next(
                (step_index for step_index, (actual, exp) in enumerate(zip(actual_outputs, expected)) if not deep_equal(actual, exp)),
                len(actual_outputs) - 1,
            )
            print(
                f"  FAIL case {index} step {step + 1}: "
                f"expected {expected[step]!r}, got {actual_outputs[step]!r}"
            )

    return passed, total


def is_wiggle(nums: list[int]) -> bool:
    for index in range(len(nums) - 1):
        if index % 2 == 0:
            if nums[index] >= nums[index + 1]:
                return False
        elif nums[index] <= nums[index + 1]:
            return False
    return True


class MockRobot:
    """Simulates LeetCode's Robot API for problem 0489."""

    _DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, room: list[list[int]], row: int, col: int):
        self.room = room
        self.row = row
        self.col = col
        self.direction = 0
        self.cleaned: set[tuple[int, int]] = set()

    def move(self) -> bool:
        dr, dc = self._DIRS[self.direction]
        nr, nc = self.row + dr, self.col + dc
        if 0 <= nr < len(self.room) and 0 <= nc < len(self.room[0]) and self.room[nr][nc] == 1:
            self.row, self.col = nr, nc
            return True
        return False

    def turnLeft(self) -> None:
        self.direction = (self.direction + 3) % 4

    def turnRight(self) -> None:
        self.direction = (self.direction + 1) % 4

    def clean(self) -> None:
        self.cleaned.add((self.row, self.col))


def robot_cleaned_all(robot: MockRobot) -> bool:
    for r, row in enumerate(robot.room):
        for c, cell in enumerate(row):
            if cell == 1 and (r, c) not in robot.cleaned:
                return False
    return True


class MockMaster:
    """Simulates LeetCode's Master API for problem 0843."""

    def __init__(self, secret: str, words: list[str], allowed_guesses: int):
        self.secret = secret
        self.words = set(words)
        self.allowed_guesses = allowed_guesses
        self.guesses = 0
        self.found = False

    def guess(self, word: str) -> int:
        self.guesses += 1
        if word not in self.words:
            return -1
        matches = sum(a == b for a, b in zip(word, self.secret))
        if matches == len(self.secret):
            self.found = True
        return matches

    def result_message(self) -> str:
        if self.found and self.guesses <= self.allowed_guesses:
            return "You guessed the secret word correctly."
        return "Either you took too many guesses, or you did not find the secret word."


class MockMountainArray:
    """Simulates LeetCode's MountainArray API for problem 1095."""

    def __init__(self, values: list[int]):
        self._values = values

    def get(self, index: int) -> int:
        return self._values[index]

    def length(self) -> int:
        return len(self._values)


class MockGridMaster:
    """Simulates LeetCode's GridMaster API for problem 1778."""

    _DELTA = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0
        self.row = 0
        self.col = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == -1:
                    self.row, self.col = r, c
                    return

    def canMove(self, direction: str) -> bool:
        dr, dc = self._DELTA[direction]
        nr, nc = self.row + dr, self.col + dc
        if not (0 <= nr < self.rows and 0 <= nc < self.cols):
            return False
        return self.grid[nr][nc] != 0

    def move(self, direction: str) -> None:
        if not self.canMove(direction):
            return
        dr, dc = self._DELTA[direction]
        self.row += dr
        self.col += dc

    def isTarget(self) -> bool:
        return self.grid[self.row][self.col] == 2


class _PrintCapture:
    def __init__(self) -> None:
        self.parts: list[str] = []

    def write(self, text: str) -> int:
        self.parts.append(text)
        return len(text)

    def flush(self) -> None:
        return None

    def output(self) -> str:
        return "".join(self.parts)


def run_print_in_order(module: Any, nums: list[int]) -> str:
    foo = module.Foo()
    methods = {1: foo.first, 2: foo.second, 3: foo.third}
    capture = _PrintCapture()
    threads = []
    for idx in nums:
        thread = threading.Thread(target=methods[idx], args=(capture,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join(timeout=5)
    return capture.output()


def run_print_foobar(module: Any, n: int) -> str:
    foobar = module.FooBar(n)
    capture = _PrintCapture()
    threads = [
        threading.Thread(target=foobar.foo, args=(capture,)),
        threading.Thread(target=foobar.bar, args=(capture,)),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=5)
    return capture.output()


def run_zero_even_odd(module: Any, n: int) -> str:
    zeo = module.ZeroEvenOdd(n)
    capture = _PrintCapture()

    def print_number(value: int) -> None:
        capture.write(str(value))

    threads = [
        threading.Thread(target=zeo.zero, args=(print_number,)),
        threading.Thread(target=zeo.even, args=(print_number,)),
        threading.Thread(target=zeo.odd, args=(print_number,)),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=5)
    return capture.output()


def run_h2o(module: Any, water: str) -> str:
    h2o = module.H2O()
    capture = _PrintCapture()

    def release_hydrogen() -> None:
        capture.write("H")

    def release_oxygen() -> None:
        capture.write("O")

    threads = []
    for ch in water:
        if ch == "H":
            threads.append(threading.Thread(target=h2o.hydrogen, args=(release_hydrogen,)))
        else:
            threads.append(threading.Thread(target=h2o.oxygen, args=(release_oxygen,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=5)
    return capture.output()


def is_valid_h2o_output(actual: str, water: str) -> bool:
    if len(actual) != len(water):
        return False
    if actual.count("H") != water.count("H") or actual.count("O") != water.count("O"):
        return False
    for i in range(0, len(actual), 3):
        group = actual[i : i + 3]
        if len(group) != 3 or group.count("H") != 2 or group.count("O") != 1:
            return False
    return True


def run_fizz_buzz(module: Any, n: int) -> list[Any]:
    fb = module.FizzBuzz(n)
    results: list[Any] = []
    lock = threading.Lock()

    def print_fizz() -> None:
        with lock:
            results.append("fizz")

    def print_buzz() -> None:
        with lock:
            results.append("buzz")

    def print_fizzbuzz() -> None:
        with lock:
            results.append("fizzbuzz")

    def print_number(value: int) -> None:
        with lock:
            results.append(value)

    threads = [
        threading.Thread(target=fb.fizz, args=(print_fizz,)),
        threading.Thread(target=fb.buzz, args=(print_buzz,)),
        threading.Thread(target=fb.fizzbuzz, args=(print_fizzbuzz,)),
        threading.Thread(target=fb.number, args=(print_number,)),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=5)
    return results


class MockHtmlParser:
    def __init__(self, urls: list[str], edges: list[list[int]]):
        self.graph: dict[str, list[str]] = {url: [] for url in urls}
        for src, dst in edges:
            self.graph[urls[src]].append(urls[dst])

    def getUrls(self, url: str) -> list[str]:
        return list(self.graph.get(url, []))


class MockCustomFunction:
    def __init__(self, function_id: int):
        self.function_id = function_id

    def f(self, x: int, y: int) -> int:
        if self.function_id == 1:
            return x + y
        return x * y


class MockImmutableListNode:
    def __init__(self, val: int, next_node: "MockImmutableListNode | None" = None):
        self.val = val
        self._next = next_node
        self._printed: list[int] | None = None

    def printValue(self) -> None:
        if self._printed is not None:
            self._printed.append(self.val)

    def getNext(self) -> "MockImmutableListNode | None":
        return self._next


def list_to_immutable_list(values: list[int], sink: list[int]) -> MockImmutableListNode | None:
    head: MockImmutableListNode | None = None
    for value in reversed(values):
        head = MockImmutableListNode(value, head)
    node = head
    while node:
        node._printed = sink
        node = node._next
    return head


class MockSea:
    def __init__(self, ships: list[list[int]]):
        self.ships = {tuple(ship) for ship in ships}

    def hasShips(self, topRight: list[int], bottomLeft: list[int]) -> bool:
        tx, ty = topRight
        bx, by = bottomLeft
        return any(bx <= x <= tx and by <= y <= ty for x, y in self.ships)


def run_dining_philosophers(module: Any, n: int) -> list[list[int]]:
    dp = module.DiningPhilosophers()
    events: list[list[int]] = []
    lock = threading.Lock()

    def make_callbacks(philosopher: int):
        left = philosopher
        right = (philosopher + 1) % 5

        def pick_left() -> None:
            with lock:
                events.append([philosopher, 1, 1])

        def pick_right() -> None:
            with lock:
                events.append([philosopher, 2, 1])

        def eat() -> None:
            with lock:
                events.append([philosopher, 0, 3])

        def put_left() -> None:
            with lock:
                events.append([philosopher, 1, 2])

        def put_right() -> None:
            with lock:
                events.append([philosopher, 2, 2])

        return pick_left, pick_right, eat, put_left, put_right

    for _ in range(n):
        threads = []
        for philosopher in range(5):
            callbacks = make_callbacks(philosopher)
            threads.append(
                threading.Thread(
                    target=dp.wantsToEat,
                    args=(philosopher, *callbacks),
                )
            )
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(timeout=5)
    return events


def is_valid_dining_events(events: list[list[int]], n: int) -> bool:
    if len(events) != 25 * n:
        return False
    eats = [0] * 5
    for philosopher, fork, action in events:
        if philosopher < 0 or philosopher > 4:
            return False
        if action == 3:
            eats[philosopher] += 1
        elif fork not in (1, 2) or action not in (1, 2):
            return False
    return eats == [n] * 5


def run_traffic_light(module: Any, cars: list[int], directions: list[int], arrival_times: list[int]) -> list[str]:
    light = module.TrafficLight()
    messages: list[str] = []
    # Process in arrival order; for equal times, keep input order.
    order = sorted(range(len(cars)), key=lambda i: (arrival_times[i], i))
    for idx in order:
        car_id = cars[idx]
        direction = directions[idx]
        road_id = 1 if direction in (1, 2) else 2
        road_name = "A" if road_id == 1 else "B"

        def turn_green(rid=road_id, name=road_name) -> None:
            messages.append(f"Traffic Light On Road {name} Is Green")

        def cross_car(cid=car_id, name=road_name, direction=direction) -> None:
            messages.append(f"Car {cid} Has Passed Road {name} In Direction {direction}")

        light.carArrived(car_id, road_id, direction, turn_green, cross_car)
    return messages


def is_valid_sort_items(order: list[int], n: int, group: list[int], before_items: list[list[int]]) -> bool:
    if not order:
        return False
    if sorted(order) != list(range(n)):
        return False
    position = {item: i for i, item in enumerate(order)}
    for item, befores in enumerate(before_items):
        for pre in befores:
            if position[pre] >= position[item]:
                return False
    # Items in the same real group must be contiguous.
    seen_groups: list[int] = []
    current = None
    active: set[int] = set()
    for item in order:
        g = group[item]
        if g == -1:
            continue
        if g != current:
            if g in active:
                return False
            active.add(g)
            current = g
    return True


def is_valid_gray_code(order: list[int], n: int, start: int) -> bool:
    if sorted(order) != list(range(1 << n)):
        return False
    if order[0] != start:
        return False
    for i in range(len(order)):
        a = order[i]
        b = order[(i + 1) % len(order)]
        if bin(a ^ b).count("1") != 1:
            return False
    return True


def is_valid_traffic_light(messages: list[str], cars: list[int], directions: list[int]) -> bool:
    expected_pass = set()
    for car, direction in zip(cars, directions):
        road = "A" if direction in (1, 2) else "B"
        expected_pass.add(f"Car {car} Has Passed Road {road} In Direction {direction}")
    green = "A"
    seen_pass = set()
    for msg in messages:
        if msg.startswith("Traffic Light On Road"):
            green = msg.split()[4]
        elif msg.startswith("Car "):
            parts = msg.split()
            road = parts[5]
            if road != green:
                return False
            seen_pass.add(msg)
        else:
            return False
    return seen_pass == expected_pass


def is_valid_max_depth_split(seq: str, bits: list[int]) -> bool:
    if len(bits) != len(seq):
        return False

    def depth_of(chars: str) -> int | None:
        cur = 0
        best = 0
        for ch in chars:
            cur += 1 if ch == "(" else -1
            if cur < 0:
                return None
            best = max(best, cur)
        return best if cur == 0 else None

    a = "".join(ch for ch, bit in zip(seq, bits) if bit == 0)
    b = "".join(ch for ch, bit in zip(seq, bits) if bit == 1)
    da = depth_of(a)
    db = depth_of(b)
    total_depth = depth_of(seq)
    if da is None or db is None or total_depth is None:
        return False
    optimal = (total_depth + 1) // 2
    return max(da, db) == optimal


def run_cases(
    solution: Any, config: dict[str, Any], cases_doc: dict[str, Any], module: Any | None = None
) -> tuple[int, int]:
    method_name = config["method"]
    arg_types = config.get("types") or {}
    return_type = arg_types.get("return")
    passed = 0
    total = len(cases_doc.get("cases", []))

    for index, case in enumerate(cases_doc.get("cases", []), start=1):
        if is_design_case(case):
            print(f"  SKIP case {index}: use design test runner")
            continue

        args = case.get("args", {})
        positional = case.get("input")
        expected = case["expected"]
        keys: list[str] = []
        values: list[Any] = []
        nary_tree_compare = False

        cycle_head = None
        if args and "listA" in args and "listB" in args and method_name == "getIntersectionNode":
            method = getattr(solution, method_name)
            head_a, head_b = build_intersection_lists(args)
            actual = method(head_a, head_b)
            actual = intersectnode_to_string(actual)
        elif args and "root" in args and "p" in args and "q" in args and method_name == "lowestCommonAncestor":
            method = getattr(solution, method_name)
            root = list_to_tree(args["root"])
            p_node = find_tree_node(root, args["p"])
            q_node = find_tree_node(root, args["q"])
            result = method(root, p_node, q_node)
            actual = result.val if result else None
        elif args and "root" in args and "nodes" in args and method_name == "lowestCommonAncestor":
            method = getattr(solution, method_name)
            root = list_to_tree(args["root"])
            node_list = [find_tree_node(root, value) for value in args["nodes"]]
            result = method(root, node_list)
            actual = result.val if result else None
        elif args and method_name == "correctBinaryTree" and "fromNode" in args and "toNode" in args:
            method = getattr(solution, method_name)
            root = list_to_tree(args["root"])
            from_node = find_tree_node(root, args["fromNode"])
            to_node = find_tree_node(root, args["toNode"])
            from_node.right = to_node
            actual = tree_to_list(method(root))
        elif args and method_name == "flipBinaryTree" and "leaf" in args:
            method = getattr(solution, method_name)
            # Build Node tree with parent pointers from level-order array.
            values = args["root"]
            if not values:
                actual = []
            else:
                class _PNode:
                    def __init__(self, val=0):
                        self.val = val
                        self.left = None
                        self.right = None
                        self.parent = None

                nodes = [_PNode(v) if v is not None else None for v in values]
                for i, node in enumerate(nodes):
                    if node is None:
                        continue
                    left_i, right_i = 2 * i + 1, 2 * i + 2
                    if left_i < len(nodes) and nodes[left_i] is not None:
                        node.left = nodes[left_i]
                        nodes[left_i].parent = node
                    if right_i < len(nodes) and nodes[right_i] is not None:
                        node.right = nodes[right_i]
                        nodes[right_i].parent = node
                root = nodes[0]
                leaf = next(n for n in nodes if n is not None and n.val == args["leaf"])
                actual = tree_to_list(method(root, leaf))
        elif args and "root" in args and "target" in args and method_name == "distanceK":
            method = getattr(solution, method_name)
            root = list_to_tree(args["root"])
            target = find_tree_node(root, args["target"])
            actual = method(root, target, args["k"])
        elif args and "head" in args and "node" in args and method_name == "deleteNode":
            method = getattr(solution, method_name)
            head = list_to_listnode(args["head"])
            target = find_list_node(head, args["node"])
            method(target)
            actual = listnode_to_list(head)
        elif args and "dummy_input" in args:
            encoded = solution.encode(args["dummy_input"])
            actual = solution.decode(encoded)
        elif method_name == "rand10" and module is not None and "n" in args:
            sequence = case.get("rand7Sequence", [])
            iterator = iter(sequence)

            def rand7() -> int:
                return next(iterator)

            module.rand7 = rand7
            actual = [solution.rand10() for _ in range(args["n"])]
        elif (
            args
            and "root" in args
            and method_name == "encodeNaryTree"
            and arg_types.get("root") == "narynode"
        ):
            root = list_to_nary(args["root"])
            binary = solution.encodeNaryTree(root)
            actual = solution.decodeBinaryTree(binary)
            expected = root
            nary_tree_compare = True
        elif (
            args
            and "root" in args
            and config.get("class") == "Codec"
            and arg_types.get("root") == "narynode"
            and module is not None
        ):
            codec = module.Codec()
            root = list_to_nary(args["root"])
            actual = codec.deserialize(codec.encode(root))
            expected = root
            nary_tree_compare = True
        elif (
            args
            and "root" in args
            and config.get("class") == "Codec"
            and "p" not in args
            and "q" not in args
        ):
            root = list_to_tree(args["root"])
            actual = tree_to_list(solution.deserialize(solution.serialize(root)))
        elif args and "root" in args and method_name == "treeToDoublyList":
            method = getattr(solution, method_name)
            root = list_to_tree(args["root"])
            actual = doubly_tree_node_to_list(method(root))
        elif args and "grid" in args and method_name == "construct":
            method = getattr(solution, method_name)
            actual = quad_tree_to_list(method(args["grid"]))
        elif args and "root" in args and method_name == "levelOrder" and arg_types.get("root") == "narynode":
            method = getattr(solution, method_name)
            actual = method(list_to_nary(args["root"]))
        elif args and method_name == "findRoot" and "tree" in args:
            method = getattr(solution, method_name)
            root = list_to_nary(args["tree"])
            nodes: list[Any] = []
            stack = [root] if root is not None else []
            while stack:
                node = stack.pop()
                nodes.append(node)
                stack.extend(node.children)
            actual = nary_to_list(method(nodes))
        elif args and method_name == "moveSubTree" and "root" in args:
            method = getattr(solution, method_name)
            root = list_to_nary(args["root"])
            by_val: dict[Any, Any] = {}
            stack = [root] if root is not None else []
            while stack:
                node = stack.pop()
                by_val[node.val] = node
                stack.extend(node.children)
            actual = nary_to_list(method(root, by_val[args["p"]], by_val[args["q"]]))
        elif args and method_name == "diameter" and "root" in args and arg_types.get("root") == "narynode":
            method = getattr(solution, method_name)
            actual = method(list_to_nary(args["root"]))
        elif args and "head" in args and method_name == "flatten" and arg_types.get("head") == "multilevelnode":
            method = getattr(solution, method_name)
            head = list_to_multilevel(args["head"])
            actual = multilevel_to_list(method(head))
        elif args and "v1" in args and "v2" in args and config.get("class") == "ZigzagIterator" and module is not None:
            iterator = module.ZigzagIterator(args["v1"], args["v2"])
            actual = []
            while iterator.hasNext():
                actual.append(iterator.next())
        elif (
            args
            and "nestedList" in args
            and config.get("class") == "NestedIterator"
            and module is not None
        ):
            iterator = module.NestedIterator(json_to_nested_list(args["nestedList"]))
            actual = []
            while iterator.hasNext():
                actual.append(iterator.next())
        elif args and "root" in args and "p" in args and method_name == "inorderSuccessor":
            method = getattr(solution, method_name)
            root = list_to_tree(args["root"])
            p_node = find_tree_node(root, args["p"])
            result = method(root, p_node)
            actual = result.val if result else None
        elif args and "tree" in args and "node" in args and method_name == "inorderSuccessor":
            method = getattr(solution, method_name)
            root = list_to_parent_tree(args["tree"])
            target = find_parent_node(root, args["node"])
            result = method(target)
            actual = result.val if result else None
        elif args and "pick" in args and method_name == "guessNumber" and module is not None:
            method = getattr(solution, method_name)
            pick = args["pick"]

            def guess(num: int) -> int:
                if num > pick:
                    return -1
                if num < pick:
                    return 1
                return 0

            module.guess = guess
            actual = method(args["n"])
        elif args and "bad" in args and method_name == "firstBadVersion" and module is not None:
            method = getattr(solution, method_name)
            bad = args["bad"]

            def is_bad_version(version: int) -> bool:
                return version >= bad

            module.isBadVersion = is_bad_version
            actual = method(args["n"])
        elif args and "graph" in args and method_name == "findCelebrity" and module is not None:
            method = getattr(solution, method_name)
            graph = args["graph"]

            def knows(person_a: int, person_b: int) -> bool:
                return graph[person_a][person_b] == 1

            module.knows = knows
            actual = method(len(graph))
        elif args and "room" in args and method_name == "cleanRoom":
            method = getattr(solution, method_name)
            robot = MockRobot(args["room"], args["row"], args["col"])
            method(robot)
            actual = "Robot cleaned all rooms." if robot_cleaned_all(robot) else "Robot missed rooms."
        elif (
            args
            and "secret" in args
            and "words" in args
            and method_name == "findSecretWord"
        ):
            method = getattr(solution, method_name)
            master = MockMaster(args["secret"], args["words"], args["allowedGuesses"])
            method(args["words"], master)
            actual = master.result_message()
        elif args and "mountainArr" in args and method_name == "findInMountainArray":
            method = getattr(solution, method_name)
            mountain = MockMountainArray(args["mountainArr"])
            actual = method(args["target"], mountain)
        elif args and "grid" in args and method_name == "findShortestPath":
            method = getattr(solution, method_name)
            master = MockGridMaster(args["grid"])
            actual = method(master)
        elif module is not None and config.get("class") == "Foo" and "nums" in args:
            actual = run_print_in_order(module, args["nums"])
        elif module is not None and config.get("class") == "FooBar" and "n" in args:
            actual = run_print_foobar(module, args["n"])
        elif module is not None and config.get("class") == "ZeroEvenOdd" and "n" in args:
            actual = run_zero_even_odd(module, args["n"])
        elif module is not None and config.get("class") == "H2O" and "water" in args:
            actual = run_h2o(module, args["water"])
        elif module is not None and config.get("class") == "FizzBuzz" and "n" in args:
            actual = run_fizz_buzz(module, args["n"])
        elif module is not None and config.get("class") == "DiningPhilosophers" and "n" in args:
            actual = run_dining_philosophers(module, args["n"])
        elif (
            module is not None
            and config.get("class") == "TrafficLight"
            and "cars" in args
            and "directions" in args
            and "arrivalTimes" in args
        ):
            actual = run_traffic_light(
                module, args["cars"], args["directions"], args["arrivalTimes"]
            )
        elif args and method_name == "crawl" and "urls" in args and "edges" in args:
            method = getattr(solution, method_name)
            parser = MockHtmlParser(args["urls"], args["edges"])
            actual = method(args["startUrl"], parser)
        elif args and method_name == "findSolution" and "function_id" in args:
            method = getattr(solution, method_name)
            custom = MockCustomFunction(args["function_id"])
            actual = method(custom, args["z"])
        elif args and method_name == "countShips" and "ans" in args:
            method = getattr(solution, method_name)
            sea = MockSea(args["ans"])
            actual = method(sea, args["topRight"], args["bottomLeft"])
        elif args and method_name == "printLinkedListInReverse" and "head" in args:
            method = getattr(solution, method_name)
            printed: list[int] = []
            head = list_to_immutable_list(args["head"], printed)
            method(head)
            actual = printed
        elif (
            args
            and config.get("class") == "Codec"
            and ("url" in args or "longUrl" in args)
            and module is not None
        ):
            long_url = args.get("url") or args.get("longUrl")
            codec = module.Codec()
            actual = codec.decode(codec.encode(long_url))
        elif args:
            method = getattr(solution, method_name)
            keys = [key for key in (config.get("paramOrder") or list(args.keys())) if key != "pos"]
            values = []
            for key in keys:
                if arg_types.get(key) == "cyclelistnode":
                    cycle_head = list_to_cyclelist(args[key], args.get("pos", -1))
                    values.append(cycle_head)
                else:
                    values.append(convert_arg(args[key], arg_types.get(key)))
            if "nums" in keys and (is_inplace_expected(expected) or return_type == "void"):
                nums_index = keys.index("nums")
                values[nums_index] = list(values[nums_index])
            if "arr" in keys and return_type == "void":
                arr_index = keys.index("arr")
                values[arr_index] = list(values[arr_index])
            if "chars" in keys and is_inplace_expected(expected):
                chars_index = keys.index("chars")
                values[chars_index] = list(values[chars_index])
            if "s" in keys and return_type == "void" and isinstance(args.get("s"), list):
                s_index = keys.index("s")
                values[s_index] = list(values[s_index])
            if "nums1" in keys and return_type == "void":
                nums1_index = keys.index("nums1")
                values[nums1_index] = list(values[nums1_index])
            if "board" in keys and return_type == "void":
                board_index = keys.index("board")
                values[board_index] = [row[:] for row in values[board_index]]
            if "rooms" in keys and return_type == "void":
                rooms_index = keys.index("rooms")
                values[rooms_index] = [row[:] for row in values[rooms_index]]
            if "matrix" in keys and return_type == "void":
                matrix_index = keys.index("matrix")
                values[matrix_index] = [row[:] for row in values[matrix_index]]
            actual = method(*values)
            if return_type == "void" and args:
                actual = void_mutation_result(keys, values)
            elif return_type == "cycleentry":
                actual = cycleentry_to_string(actual, cycle_head)
            else:
                actual = convert_result(actual, return_type)
        elif positional is not None:
            method = getattr(solution, method_name)
            actual = method(*positional)
            actual = convert_result(actual, return_type)
        else:
            method = getattr(solution, method_name)
            actual = method()
            actual = convert_result(actual, return_type)

        if is_inplace_expected(expected):
            parsed = parse_inplace_expected(expected)
            if parsed is None:
                print(f"  FAIL case {index}: unable to parse inplace expected {expected!r}")
                continue
            expected_count, expected_prefix = parsed
            nums_index = keys.index("nums") if args and "nums" in keys else None
            chars_index = keys.index("chars") if args and "chars" in keys else None
            nums_after = values[nums_index] if nums_index is not None else None
            chars_after = values[chars_index] if chars_index is not None else None
            mutated = nums_after if nums_after is not None else chars_after
            ok = (
                actual == expected_count
                and mutated is not None
                and mutated[:expected_count] == expected_prefix
            )
        elif method_name == "wiggleSort" and isinstance(actual, list) and is_wiggle(actual):
            ok = True
        elif method_name == "shortestSuperstring" and isinstance(actual, str):
            ok = len(actual) == len(expected) and all(w in actual for w in args.get("words", []))
        elif method_name == "strWithout3a3b" and isinstance(actual, str):
            ok = (
                actual.count("a") == args.get("a")
                and actual.count("b") == args.get("b")
                and "aaa" not in actual
                and "bbb" not in actual
            )
        elif method_name == "pancakeSort" and isinstance(actual, list):
            # Use a fresh copy; solution may also leave args untouched.
            start = list(cases_doc["cases"][index - 1]["args"]["arr"])
            for k in actual:
                start[:k] = start[:k][::-1]
            ok = start == sorted(start)
        elif config.get("class") == "H2O" and isinstance(actual, str):
            ok = is_valid_h2o_output(actual, args.get("water", ""))
        elif config.get("class") == "DiningPhilosophers" and isinstance(actual, list):
            ok = is_valid_dining_events(actual, args.get("n", 1))
        elif config.get("class") == "TrafficLight" and isinstance(actual, list):
            ok = is_valid_traffic_light(actual, args.get("cars", []), args.get("directions", []))
        elif method_name == "getLonelyNodes" and isinstance(actual, list) and isinstance(expected, list):
            ok = sorted(actual) == sorted(expected)
        elif method_name == "findCriticalAndPseudoCriticalEdges" and isinstance(actual, list):
            ok = (
                isinstance(expected, list)
                and len(actual) == 2
                and len(expected) == 2
                and sorted(actual[0]) == sorted(expected[0])
                and sorted(actual[1]) == sorted(expected[1])
            )
        elif method_name == "sortItems" and isinstance(actual, list):
            ok = is_valid_sort_items(
                actual, args.get("n", 0), args.get("group", []), args.get("beforeItems", [])
            ) if expected else actual == expected
        elif method_name == "circularPermutation" and isinstance(actual, list):
            ok = is_valid_gray_code(actual, args.get("n", 0), args.get("start", 0))
        elif method_name == "maxDepthAfterSplit" and isinstance(actual, list):
            ok = is_valid_max_depth_split(args.get("seq", ""), actual)
        elif method_name == "generateTheString" and isinstance(actual, str):
            counts = {char: actual.count(char) for char in set(actual)}
            ok = len(actual) == args.get("n") and all(count % 2 == 1 for count in counts.values())
        elif method_name == "balanceBST" and isinstance(actual, list):
            tree = list_to_tree(actual)

            def balanced_height(node: TreeNode | None) -> int:
                if node is None:
                    return 0
                left_height = balanced_height(node.left)
                right_height = balanced_height(node.right)
                if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
                    return -1
                return max(left_height, right_height) + 1

            original_values = sorted(value for value in args.get("root", []) if value is not None)
            actual_values = sorted(value for value in actual if value is not None)
            ok = original_values == actual_values and balanced_height(tree) >= 0
        elif method_name == "closestDivisors" and isinstance(actual, list):
            ok = sorted(actual) == sorted(expected)
        elif return_type in {"treenode[]", "string[][]", "string[]", "integer[][]", "integer[]"}:
            ok = trees_equal_any_order(actual, expected)
        elif nary_tree_compare:
            ok = nary_trees_equal(actual, expected)
        elif deep_equal(actual, expected):
            ok = True
        else:
            ok = False

        if ok:
            passed += 1
            print(f"  PASS case {index}")
        else:
            print(f"  FAIL case {index}: expected {expected!r}, got {actual!r}")

    return passed, total
