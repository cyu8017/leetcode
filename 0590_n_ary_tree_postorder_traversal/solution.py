# LeetCode 0590 - N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

from typing import List


class Node:
    def __init__(self, val: int | None = None, children: list["Node"] | None = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def postorder(self, root: "Node | None") -> List[int]:
        result: list[int] = []

        def dfs(node: "Node | None") -> None:
            if not node:
                return
            for child in node.children:
                dfs(child)
            result.append(node.val)

        dfs(root)
        return result
