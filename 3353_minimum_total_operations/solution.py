# LeetCode 3353 - Minimum Total Operations
# https://leetcode.com/problems/minimum-total-operations/

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] != nums[i + 1]:
                ops += 1
        return ops
