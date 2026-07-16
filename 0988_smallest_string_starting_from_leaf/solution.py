# LeetCode 0988 - Smallest String Starting From Leaf
# https://leetcode.com/problems/smallest-string-starting-from-leaf/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.best = "~"

        def dfs(node: Optional[TreeNode], path: str) -> None:
            if not node:
                return
            path = chr(ord("a") + node.val) + path
            if not node.left and not node.right:
                self.best = min(self.best, path)
                return
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return self.best
