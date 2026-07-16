# LeetCode 0606 - Construct String from Binary Tree
# https://leetcode.com/problems/construct-string-from-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        result = str(root.val)
        if root.left or root.right:
            result += f"({self.tree2str(root.left)})"
        if root.right:
            result += f"({self.tree2str(root.right)})"
        return result
