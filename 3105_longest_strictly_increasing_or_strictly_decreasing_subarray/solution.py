# LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        t = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                t += 1
                ans = max(ans, t)
            else:
                t = 1
        t = 1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                t += 1
                ans = max(ans, t)
            else:
                t = 1
        return ans
