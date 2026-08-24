# LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 1000000007
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for r in range(k):
                    if dp[i][j][r] == 0:
                        continue
                    if i + 1 < m:
                        nr = (r + grid[i + 1][j]) % k
                        dp[i + 1][j][nr] = (dp[i + 1][j][nr] + dp[i][j][r]) % mod
                    if j + 1 < n:
                        nr = (r + grid[i][j + 1]) % k
                        dp[i][j + 1][nr] = (dp[i][j + 1][nr] + dp[i][j][r]) % mod
        return dp[m - 1][n - 1][0]
