# LeetCode 3989 - Maximum Consistent Columns in a Grid
# https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

from typing import List


class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        ans = 1
        for j in range(n):
            dp[j] = 1
            for i in range(j):
                if dp[i] + 1 <= dp[j]:
                    continue
                ok = True
                for r in range(m):
                    d = abs(grid[r][j] - grid[r][i])
                    if d > limit:
                        ok = False
                        break
                if ok:
                    dp[j] = dp[i] + 1
            if dp[j] > ans:
                ans = dp[j]
        return ans
