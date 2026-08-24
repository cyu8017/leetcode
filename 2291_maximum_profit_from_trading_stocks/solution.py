# LeetCode 2291 - Maximum Profit From Trading Stocks
# https://leetcode.com/problems/maximum-profit-from-trading-stocks/

from typing import List


class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n = len(present)
        dp = [0] * (budget + 1)
        for i in range(n):
            profit = future[i] - present[i]
            if profit <= 0:
                continue
            cost = present[i]
            for b in range(budget, cost - 1, -1):
                dp[b] = max(dp[b], dp[b - cost] + profit)
        return dp[budget]
