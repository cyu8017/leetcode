# LeetCode 2706 - Buy Two Chocolates
# https://leetcode.com/problems/buy-two-chocolates/

from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        cost = prices[0] + prices[1]
        return money - cost if cost <= money else money
