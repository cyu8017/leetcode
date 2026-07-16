# LeetCode 0413 - Arithmetic Slices
# https://leetcode.com/problems/arithmetic-slices/

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        total = 0
        current = 0
        for index in range(2, len(nums)):
            if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]:
                current += 1
                total += current
            else:
                current = 0
        return total
