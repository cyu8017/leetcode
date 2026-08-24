# LeetCode 3473 - Sum of K Subarrays With Length at Least M
# https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        neg = -(10**18)
        dp = [[neg] * (n + 1) for _ in range(k + 1)]
        for i in range(n + 1):
            dp[0][i] = 0
        for t in range(1, k + 1):
            best = neg
            for i in range(t * m, n + 1):
                j = i - m
                best = max(best, dp[t - 1][j] - pref[j])
                dp[t][i] = best + pref[i]
            for i in range(1, n + 1):
                dp[t][i] = max(dp[t][i], dp[t][i - 1])
        return dp[k][n]
