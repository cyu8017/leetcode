# LeetCode 0188 - Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        if k >= n // 2:
            return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))

        buy = [float("inf")] * (k + 1)
        sell = [0] * (k + 1)
        for price in prices:
            for t in range(1, k + 1):
                buy[t] = min(buy[t], price - sell[t - 1])
                sell[t] = max(sell[t], price - buy[t])
        return sell[k]
