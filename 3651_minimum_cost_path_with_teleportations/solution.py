# LeetCode 3651 - Minimum Cost Path with Teleportations
# https://leetcode.com/problems/minimum-cost-path-with-teleportations/

from typing import List


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        inf = 536870911
        f = [[[inf] * n for _ in range(m)] for _ in range(k + 1)]
        f[0][0][0] = 0
        for i in range(m):
            for j in range(n):
                if i > 0:
                    f[0][i][j] = min(f[0][i][j], f[0][i - 1][j] + grid[i][j])
                if j > 0:
                    f[0][i][j] = min(f[0][i][j], f[0][i][j - 1] + grid[i][j])
        g = {}
        for i in range(m):
            for j in range(n):
                g.setdefault(grid[i][j], []).append((i, j))
        keys = sorted(g.keys(), reverse=True)
        for t in range(1, k + 1):
            mn = inf
            for key in keys:
                pos = g[key]
                for p in pos:
                    mn = min(mn, f[t - 1][p[0]][p[1]])
                for p in pos:
                    f[t][p[0]][p[1]] = mn
            for i in range(m):
                for j in range(n):
                    if i > 0:
                        f[t][i][j] = min(f[t][i][j], f[t][i - 1][j] + grid[i][j])
                    if j > 0:
                        f[t][i][j] = min(f[t][i][j], f[t][i][j - 1] + grid[i][j])
        ans = inf
        for t in range(k + 1):
            ans = min(ans, f[t][m - 1][n - 1])
        return ans
