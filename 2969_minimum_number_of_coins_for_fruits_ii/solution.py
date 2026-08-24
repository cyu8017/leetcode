# LeetCode 2969 - Minimum Number of Coins for Fruits II
# https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [1 << 30] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = i
            while j <= n and j <= 2 * i:
                dp[j] = min(dp[j], dp[i - 1] + prices[i - 1])
                j += 1
        return dp[n]
