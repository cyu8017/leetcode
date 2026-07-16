# LeetCode 0543 - Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def depth(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            best = max(best, left + right)
            return 1 + max(left, right)

        depth(root)
        return best
