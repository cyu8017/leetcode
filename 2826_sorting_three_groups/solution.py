# LeetCode 2826 - Sorting Three Groups
# https://leetcode.com/problems/sorting-three-groups/

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**9
        dp = [[INF] * 4 for _ in range(n + 1)]
        dp[0][1] = dp[0][2] = dp[0][3] = 0
        for i in range(1, n + 1):
            v = nums[i - 1]
            for g in range(1, 4):
                cost = 0 if v == g else 1
                for prev in range(1, g + 1):
                    dp[i][g] = min(dp[i][g], dp[i - 1][prev] + cost)
        return min(dp[n][1], dp[n][2], dp[n][3])
