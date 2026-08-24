# LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

from typing import List


class Solution:
    def minCost(
        self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]
    ) -> int:
        ans = 0
        sr, sc = startPos
        hr, hc = homePos
        if sr < hr:
            for r in range(sr + 1, hr + 1):
                ans += rowCosts[r]
        else:
            for r in range(sr - 1, hr - 1, -1):
                ans += rowCosts[r]
        if sc < hc:
            for c in range(sc + 1, hc + 1):
                ans += colCosts[c]
        else:
            for c in range(sc - 1, hc - 1, -1):
                ans += colCosts[c]
        return ans
