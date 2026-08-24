# LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
# https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)
        dp[0] = 0
        for v in nums:
            for s in range(target, v - 1, -1):
                if dp[s - v] >= 0 and dp[s - v] + 1 > dp[s]:
                    dp[s] = dp[s - v] + 1
        return dp[target]
