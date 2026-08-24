# LeetCode 2401 - Longest Nice Subarray
# https://leetcode.com/problems/longest-nice-subarray/

from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used = left = ans = 0
        for right in range(len(nums)):
            while (used & nums[right]) != 0:
                used ^= nums[left]
                left += 1
            used |= nums[right]
            ans = max(ans, right - left + 1)
        return ans
