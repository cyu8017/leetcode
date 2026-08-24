# LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
# https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        dp = [[0] * 301 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                d = abs(nums[i] - nums[j])
                best = 1
                for pd in range(d, 301):
                    if dp[j][pd] > best:
                        best = dp[j][pd]
                if best + 1 > dp[i][d]:
                    dp[i][d] = best + 1
                if dp[i][d] > ans:
                    ans = dp[i][d]
            if dp[i][0] < 1:
                dp[i][0] = 1
        return ans
