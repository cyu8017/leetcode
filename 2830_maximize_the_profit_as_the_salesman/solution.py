# LeetCode 2830 - Maximize the Profit as the Salesman
# https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

from typing import List


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        by_end = [[] for _ in range(n)]
        for o in offers:
            by_end[o[1]].append(o)
        dp = [0] * (n + 1)
        for end in range(n):
            dp[end + 1] = dp[end]
            for o in by_end[end]:
                dp[end + 1] = max(dp[end + 1], dp[o[0]] + o[2])
        return dp[n]
