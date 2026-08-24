# LeetCode 3418 - Maximum Amount of Money Robot Can Earn
# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        neg = -(1 << 30)
        dp = [[[neg] * 3 for _ in range(n)] for _ in range(m)]
        if coins[0][0] < 0:
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = 0
            dp[0][0][2] = 0
        else:
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = coins[0][0]
            dp[0][0][2] = coins[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for k in range(3):
                    best = neg
                    if i > 0:
                        best = max(best, dp[i - 1][j][k])
                    if j > 0:
                        best = max(best, dp[i][j - 1][k])
                    if best == neg:
                        continue
                    if coins[i][j] >= 0:
                        dp[i][j][k] = best + coins[i][j]
                    else:
                        dp[i][j][k] = max(dp[i][j][k], best + coins[i][j])
                for k in range(1, 3):
                    best = neg
                    if i > 0:
                        best = max(best, dp[i - 1][j][k - 1])
                    if j > 0:
                        best = max(best, dp[i][j - 1][k - 1])
                    if best != neg and coins[i][j] < 0:
                        dp[i][j][k] = max(dp[i][j][k], best)
        return max(dp[m - 1][n - 1][0], dp[m - 1][n - 1][1], dp[m - 1][n - 1][2])
