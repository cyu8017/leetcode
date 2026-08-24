# LeetCode 2463 - Minimum Total Distance Traveled
# https://leetcode.com/problems/minimum-total-distance-traveled/

from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robots = sorted(robot)
        factory = sorted(factory, key=lambda x: x[0])
        m = len(robots)
        pos = []
        for f in factory:
            for _ in range(f[1]):
                pos.append(f[0])
        n = len(pos)
        INF = 10**18
        dp = [[INF] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 0
        for i in range(1, m + 1):
            for j in range(i, n + 1):
                dp[i][j] = dp[i][j - 1]
                diff = robots[i - 1] - pos[j - 1]
                if diff < 0:
                    diff = -diff
                if dp[i - 1][j - 1] + diff < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - 1] + diff
        return dp[m][n]
