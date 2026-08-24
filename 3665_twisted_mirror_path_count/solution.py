# LeetCode 3665 - Twisted Mirror Path Count
# https://leetcode.com/problems/twisted-mirror-path-count/

from typing import List, Optional, Tuple


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 1000000007
        m, n = len(grid), len(grid[0])

        def next_cell(i: int, j: int, di: int, dj: int) -> Optional[Tuple[int, int]]:
            ni, nj = i + di, j + dj
            while 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                if dj == 1:
                    di, dj = 1, 0
                else:
                    di, dj = 0, 1
                ni += di
                nj += dj
            if ni < 0 or nj < 0 or ni >= m or nj >= n:
                return None
            return (ni, nj)

        dp = [[0] * n for _ in range(m)]
        if grid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or dp[i][j] == 0:
                    continue
                a = next_cell(i, j, 0, 1)
                if a:
                    dp[a[0]][a[1]] = (dp[a[0]][a[1]] + dp[i][j]) % MOD
                b = next_cell(i, j, 1, 0)
                if b:
                    dp[b[0]][b[1]] = (dp[b[0]][b[1]] + dp[i][j]) % MOD
        return dp[m - 1][n - 1]
