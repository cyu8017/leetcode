# LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: list[int]) -> list[int]:
        self.i = 0
        ans: list[int] = []

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            if node.val != voyage[self.i]:
                return False
            self.i += 1
            if node.left and node.left.val != voyage[self.i]:
                ans.append(node.val)
                return dfs(node.right) and dfs(node.left)
            return dfs(node.left) and dfs(node.right)

        return ans if dfs(root) else [-1]
