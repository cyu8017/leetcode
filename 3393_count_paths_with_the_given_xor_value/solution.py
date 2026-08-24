# LeetCode 3393 - Count Paths With the Given XOR Value
# https://leetcode.com/problems/count-paths-with-the-given-xor-value/

from typing import List


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        mod = 1000000007
        m, n = len(grid), len(grid[0])
        dp = [[[0] * 16 for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = 1
        for i in range(m):
            for j in range(n):
                for x in range(16):
                    if dp[i][j][x] == 0:
                        continue
                    if i + 1 < m:
                        nx = x ^ grid[i + 1][j]
                        dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod
                    if j + 1 < n:
                        nx = x ^ grid[i][j + 1]
                        dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod
        return dp[m - 1][n - 1][k]
