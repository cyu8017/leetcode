# LeetCode 2624 - Snail Traversal
# https://leetcode.com/problems/snail-traversal/

from typing import List


class Solution:
    def snail(self, nums: List[int], rowsCount: int, colsCount: int) -> List[List[int]]:
        if rowsCount * colsCount != len(nums):
            return []
        ans = [[0] * colsCount for _ in range(rowsCount)]
        idx = 0
        for c in range(colsCount):
            if c % 2 == 0:
                for r in range(rowsCount):
                    ans[r][c] = nums[idx]
                    idx += 1
            else:
                for r in range(rowsCount - 1, -1, -1):
                    ans[r][c] = nums[idx]
                    idx += 1
        return ans
