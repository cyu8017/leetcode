# LeetCode 2658 - Maximum Number of Fish in a Grid
# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            fish = grid[r][c]
            grid[r][c] = 0
            return fish + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        best = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    best = max(best, dfs(i, j))
        return best
