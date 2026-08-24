# LeetCode 2684 - Maximum Number of Moves in a Grid
# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * m
        for c in range(n - 2, -1, -1):
            ndp = [0] * m
            for r in range(m):
                best = 0
                for dr in (-1, 0, 1):
                    nr = r + dr
                    if 0 <= nr < m and grid[nr][c + 1] > grid[r][c]:
                        best = max(best, 1 + dp[nr])
                ndp[r] = best
            dp = ndp
        return max(dp)
