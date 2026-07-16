# LeetCode 1120 - Maximum Average Subtree
# https://leetcode.com/problems/maximum-average-subtree/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        best = 0.0

        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            nonlocal best
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            best = max(best, total_sum / total_count)
            return total_sum, total_count

        dfs(root)
        return best
