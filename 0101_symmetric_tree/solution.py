# LeetCode 0101 - Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirrors(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return mirrors(left.left, right.right) and mirrors(left.right, right.left)

        return mirrors(root.left, root.right) if root else True
