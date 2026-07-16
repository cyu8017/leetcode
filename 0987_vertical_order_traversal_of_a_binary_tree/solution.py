# LeetCode 0987 - Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        nodes: list[tuple[int, int, int]] = []

        def dfs(node: Optional[TreeNode], row: int, col: int) -> None:
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort()
        ans: dict[int, list[int]] = defaultdict(list)
        for col, _, val in nodes:
            ans[col].append(val)
        return [ans[c] for c in sorted(ans)]
