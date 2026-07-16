# LeetCode 0508 - Most Frequent Subtree Sum
# https://leetcode.com/problems/most-frequent-subtree-sum/

from collections import Counter
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> list[int]:
        counts: Counter[int] = Counter()

        def subtree_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            total = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            counts[total] += 1
            return total

        subtree_sum(root)
        if not counts:
            return []
        best = max(counts.values())
        return sorted(value for value, count in counts.items() if count == best)
