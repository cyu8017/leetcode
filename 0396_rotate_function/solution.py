# LeetCode 0396 - Rotate Function
# https://leetcode.com/problems/rotate-function/

from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        current = sum(index * value for index, value in enumerate(nums))
        best = current

        for index in range(n - 1, 0, -1):
            current += total - n * nums[index]
            best = max(best, current)

        return best
