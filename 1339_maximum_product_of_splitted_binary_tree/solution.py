# LeetCode 1339 - Maximum Product Of Splitted Binary Tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []
        def total(node):
            if not node:
                return 0
            value = node.val + total(node.left) + total(node.right)
            sums.append(value)
            return value
        whole = total(root)
        return max(value * (whole - value) for value in sums) % 1_000_000_007
