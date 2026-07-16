# LeetCode 1145 - Binary Tree Coloring Game
# https://leetcode.com/problems/binary-tree-coloring-game/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        left = right = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal left, right
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            if node.val == x:
                left, right = l, r
            return l + r + 1

        dfs(root)
        return max(left, right, n - left - right - 1) > n // 2
