# LeetCode 0270 - Closest Binary Search Tree Value
# https://leetcode.com/problems/closest-binary-search-tree-value/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        current = root
        while current:
            if abs(closest - target) > abs(current.val - target):
                closest = current.val
            if current.val == target:
                return current.val
            current = current.left if target < current.val else current.right
        return closest
