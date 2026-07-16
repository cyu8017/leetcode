# LeetCode 0589 - N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

from typing import List


class Node:
    def __init__(self, val: int | None = None, children: list["Node"] | None = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def preorder(self, root: "Node | None") -> List[int]:
        result: list[int] = []

        def dfs(node: "Node | None") -> None:
            if not node:
                return
            result.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(root)
        return result
