# LeetCode 2331 - Evaluate Boolean Binary Tree
# https://leetcode.com/problems/evaluate-boolean-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return root.val == 1
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)
        if root.val == 2:
            return l or r
        return l and r
