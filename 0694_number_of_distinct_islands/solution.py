# LeetCode 0694 - Number of Distinct Islands
# https://leetcode.com/problems/number-of-distinct-islands/

from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        shapes: set[tuple[tuple[int, int], ...]] = set()

        def dfs(r: int, c: int, br: int, bc: int, path: list[tuple[int, int]]) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            grid[r][c] = 0
            path.append((r - br, c - bc))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc, br, bc, path)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path: list[tuple[int, int]] = []
                    dfs(i, j, i, j, path)
                    shapes.add(tuple(path))
        return len(shapes)
