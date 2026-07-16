# LeetCode 0951 - Flip Equivalent Binary Trees
# https://leetcode.com/problems/flip-equivalent-binary-trees/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return (
            self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        ) or (
            self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        )
