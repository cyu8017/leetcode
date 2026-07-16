# LeetCode 0437 - Path Sum III
# https://leetcode.com/problems/path-sum-iii/

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_counts: defaultdict[int, int] = defaultdict(int)
        prefix_counts[0] = 1

        def dfs(node: Optional[TreeNode], current: int) -> int:
            if node is None:
                return 0
            current += node.val
            total = prefix_counts[current - targetSum]
            prefix_counts[current] += 1
            total += dfs(node.left, current)
            total += dfs(node.right, current)
            prefix_counts[current] -= 1
            return total

        return dfs(root, 0)
