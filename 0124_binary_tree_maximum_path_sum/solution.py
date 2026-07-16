# LeetCode 0124 - Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        def gain(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            best = max(best, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return int(best)
