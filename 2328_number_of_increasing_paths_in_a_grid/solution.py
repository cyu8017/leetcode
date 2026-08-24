# LeetCode 2328 - Number of Increasing Paths in a Grid
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 1000000007
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int) -> int:
            if dp[r][c] != 0:
                return dp[r][c]
            res = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
                    res = (res + dfs(nr, nc)) % MOD
            dp[r][c] = res
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dfs(i, j)) % MOD
        return ans
