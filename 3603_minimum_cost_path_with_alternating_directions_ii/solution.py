# LeetCode 3603 - Minimum Cost Path with Alternating Directions II
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

from typing import List


def entry3603(i: int, j: int) -> int:
    return (i + 1) * (j + 1)


class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        INF = 10**18
        dp = [[INF] * n for _ in range(m)]
        dp[0][0] = entry3603(0, 0)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i > 0:
                    cand = dp[i - 1][j] + entry3603(i, j)
                    if not (i - 1 == 0 and j == 0):
                        cand += waitCost[i - 1][j]
                    dp[i][j] = min(dp[i][j], cand)
                if j > 0:
                    cand = dp[i][j - 1] + entry3603(i, j)
                    if not (i == 0 and j - 1 == 0):
                        cand += waitCost[i][j - 1]
                    dp[i][j] = min(dp[i][j], cand)
        return dp[m - 1][n - 1]
