# LeetCode 0053 - Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            best = max(best, current)

        return best
