# LeetCode 2898 - Maximum Linear Stock Score
# https://leetcode.com/problems/maximum-linear-stock-score/

from typing import List


class Solution:
    def maxScore(self, prices: List[int]) -> int:
        best = {}
        ans = 0
        for i, price in enumerate(prices):
            key = price - (i + 1)
            cand = best.get(key, 0) + price
            if cand > best.get(key, 0):
                best[key] = cand
            if best[key] > ans:
                ans = best[key]
        return ans
