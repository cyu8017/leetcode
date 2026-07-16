# LeetCode 0718 - Maximum Length of Repeated Subarray
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)
        best = 0
        for i in range(1, m + 1):
            next_dp = [0] * (n + 1)
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    next_dp[j] = dp[j - 1] + 1
                    best = max(best, next_dp[j])
            dp = next_dp
        return best
