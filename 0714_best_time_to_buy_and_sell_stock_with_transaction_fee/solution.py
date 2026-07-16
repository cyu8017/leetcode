# LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        cash = 0
        for price in prices[1:]:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - fee)
        return cash
