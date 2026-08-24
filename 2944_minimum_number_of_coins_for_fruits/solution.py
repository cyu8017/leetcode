# LeetCode 2944 - Minimum Number of Coins for Fruits
# https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [1 << 30] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = i
            while j <= n and j <= i + i:
                cand = dp[i - 1] + prices[i - 1]
                if cand < dp[j]:
                    dp[j] = cand
                j += 1
        return dp[n]
