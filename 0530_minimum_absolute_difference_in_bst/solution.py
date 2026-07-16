# LeetCode 0530 - Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        previous = None
        best = float("inf")

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal previous, best
            if not node:
                return
            inorder(node.left)
            if previous is not None:
                best = min(best, node.val - previous)
            previous = node.val
            inorder(node.right)

        inorder(root)
        return best
