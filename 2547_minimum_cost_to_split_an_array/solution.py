# LeetCode 2547 - Minimum Cost to Split an Array
# https://leetcode.com/problems/minimum-cost-to-split-an-array/

from typing import List


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            freq = {}
            trimmed = 0
            for j in range(i, n):
                c = freq.get(nums[j], 0) + 1
                freq[nums[j]] = c
                if c == 2:
                    trimmed += 2
                elif c > 2:
                    trimmed += 1
                cost = dp[i] + k + trimmed
                if cost < dp[j + 1]:
                    dp[j + 1] = cost
        return dp[n]
