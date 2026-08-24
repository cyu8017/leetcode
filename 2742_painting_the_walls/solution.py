# LeetCode 2742 - Painting the Walls
# https://leetcode.com/problems/painting-the-walls/

from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(n, -1, -1):
                nj = min(n, j + time[i] + 1)
                if dp[j] + cost[i] < dp[nj]:
                    dp[nj] = dp[j] + cost[i]
        return dp[n]
