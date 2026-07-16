# LeetCode 0711 - Number of Distinct Islands II
# https://leetcode.com/problems/number-of-distinct-islands-ii/

from typing import List


class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        shapes: set[tuple[tuple[int, int], ...]] = set()

        def dfs(r: int, c: int, cells: list[tuple[int, int]]) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            grid[r][c] = 0
            cells.append((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc, cells)

        def canonical(cells: list[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
            transforms = [
                lambda x, y: (x, y),
                lambda x, y: (x, -y),
                lambda x, y: (-x, y),
                lambda x, y: (-x, -y),
                lambda x, y: (y, x),
                lambda x, y: (y, -x),
                lambda x, y: (-y, x),
                lambda x, y: (-y, -x),
            ]
            norms: list[tuple[tuple[int, int], ...]] = []
            for transform in transforms:
                pts = [transform(x, y) for x, y in cells]
                min_x = min(p[0] for p in pts)
                min_y = min(p[1] for p in pts)
                norms.append(tuple(sorted((p[0] - min_x, p[1] - min_y) for p in pts)))
            return min(norms)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cells: list[tuple[int, int]] = []
                    dfs(i, j, cells)
                    shapes.add(canonical(cells))
        return len(shapes)
