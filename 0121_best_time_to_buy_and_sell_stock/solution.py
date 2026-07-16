# LeetCode 0121 - Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                best = max(best, price - min_price)
        return best
