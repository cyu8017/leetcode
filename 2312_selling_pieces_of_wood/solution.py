# LeetCode 2312 - Selling Pieces of Wood
# https://leetcode.com/problems/selling-pieces-of-wood/

from typing import List


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        price = [[0] * (n + 1) for _ in range(m + 1)]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            price[h][w] = p
        for h in range(1, m + 1):
            for w in range(1, n + 1):
                best = price[h][w]
                for i in range(1, h):
                    best = max(best, dp[i][w] + dp[h - i][w])
                for j in range(1, w):
                    best = max(best, dp[h][j] + dp[h][w - j])
                dp[h][w] = best
        return dp[m][n]
