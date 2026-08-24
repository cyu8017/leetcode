# LeetCode 3742 - Maximum Path Score in a Grid
# https://leetcode.com/problems/maximum-path-score-in-a-grid/

from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        INF = 1 << 30
        m, n = len(grid), len(grid[0])
        f = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        def dfs(i: int, j: int, kk: int) -> int:
            if i < 0 or j < 0 or kk < 0:
                return -INF
            if i == 0 and j == 0:
                return 0
            if f[i][j][kk] != -1:
                return f[i][j][kk]
            res = grid[i][j]
            nk = kk
            if grid[i][j] != 0:
                nk -= 1
            a = dfs(i - 1, j, nk)
            b = dfs(i, j - 1, nk)
            res += max(a, b)
            f[i][j][kk] = res
            return res

        ans = dfs(m - 1, n - 1, k)
        return -1 if ans < 0 else ans
