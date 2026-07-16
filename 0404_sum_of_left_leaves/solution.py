# LeetCode 0404 - Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        total = 0
        if root.left and root.left.left is None and root.left.right is None:
            total += root.left.val
        else:
            total += self.sumOfLeftLeaves(root.left)

        total += self.sumOfLeftLeaves(root.right)
        return total
