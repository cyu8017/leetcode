# LeetCode 3708 - Longest Fibonacci Subarray
# https://leetcode.com/problems/longest-fibonacci-subarray/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        f = 2
        ans = f
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] + nums[i - 2]:
                f += 1
                ans = max(ans, f)
            else:
                f = 2
        return ans
