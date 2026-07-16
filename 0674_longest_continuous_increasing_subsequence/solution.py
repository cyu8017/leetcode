# LeetCode 0674 - Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        best = cur = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1
        return best
