# LeetCode 2585 - Number of Ways to Earn Points
# https://leetcode.com/problems/number-of-ways-to-earn-points/

from typing import List


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 1000000007
        dp = [0] * (target + 1)
        dp[0] = 1
        for count, marks in types:
            for s in range(target, -1, -1):
                k = 1
                while k <= count and s - k * marks >= 0:
                    dp[s] = (dp[s] + dp[s - k * marks]) % MOD
                    k += 1
        return dp[target]
