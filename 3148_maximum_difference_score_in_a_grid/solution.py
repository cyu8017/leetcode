# LeetCode 3148 - Maximum Difference Score in a Grid
# https://leetcode.com/problems/maximum-difference-score-in-a-grid/

from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        INF = 1 << 30
        f = [[0] * n for _ in range(m)]
        ans = -INF
        for i in range(m):
            for j in range(n):
                x = grid[i][j]
                mi = INF
                if i > 0:
                    mi = min(mi, f[i - 1][j])
                if j > 0:
                    mi = min(mi, f[i][j - 1])
                ans = max(ans, x - mi)
                f[i][j] = min(x, mi)
        return ans
