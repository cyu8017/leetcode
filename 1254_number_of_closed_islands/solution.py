from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def flood(sr: int, sc: int) -> bool:
            stack, closed = [(sr, sc)], True
            grid[sr][sc] = 1
            while stack:
                r, c = stack.pop()
                if r in (0, m - 1) or c in (0, n - 1):
                    closed = False
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        stack.append((nr, nc))
            return closed
        return sum(flood(r, c) for r in range(m) for c in range(n) if grid[r][c] == 0)
