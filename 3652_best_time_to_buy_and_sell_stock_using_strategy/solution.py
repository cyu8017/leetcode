# LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        s = [0] * (n + 1)
        t = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + prices[i - 1] * strategy[i - 1]
            t[i] = t[i - 1] + prices[i - 1]
        ans = s[n]
        for i in range(k, n + 1):
            ans = max(ans, s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k // 2]))
        return ans
