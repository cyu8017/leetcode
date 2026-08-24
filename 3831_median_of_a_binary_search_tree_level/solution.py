# LeetCode 3831 - Median of a Binary Search Tree Level
# https://leetcode.com/problems/median-of-a-binary-search-tree-level/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelMedian(self, root: Optional[TreeNode], level: int) -> int:
        nums: List[int] = []

        def dfs(node: Optional[TreeNode], i: int) -> None:
            if not node:
                return
            dfs(node.left, i + 1)
            if i == level:
                nums.append(node.val)
            dfs(node.right, i + 1)

        dfs(root, 0)
        if not nums:
            return -1
        return nums[len(nums) // 2]
