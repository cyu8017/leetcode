# LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        free = 0
        hold = -prices[0]
        cooldown = 0
        for price in prices[1:]:
            free, hold, cooldown = (
                max(free, cooldown),
                max(hold, free - price),
                hold + price,
            )
        return max(free, cooldown)
