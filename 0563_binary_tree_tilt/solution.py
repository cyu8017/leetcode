# LeetCode 0563 - Binary Tree Tilt
# https://leetcode.com/problems/binary-tree-tilt/

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
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = 0

        def subtree_sum(node: Optional[TreeNode]) -> int:
            nonlocal total
            if not node:
                return 0
            left = subtree_sum(node.left)
            right = subtree_sum(node.right)
            total += abs(left - right)
            return node.val + left + right

        subtree_sum(root)
        return total
