# LeetCode 2280 - Minimum Lines to Represent a Line Chart
# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) <= 1:
            return 0
        stockPrices.sort()
        ans = 1
        for i in range(2, len(stockPrices)):
            x0, y0 = stockPrices[i - 2]
            x1, y1 = stockPrices[i - 1]
            x2, y2 = stockPrices[i]
            if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0):
                ans += 1
        return ans
