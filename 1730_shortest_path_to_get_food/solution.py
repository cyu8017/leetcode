from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        seen = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    queue.append((r, c, 0))
                    seen.add((r, c))
        while queue:
            r, c, d = queue.popleft()
            if grid[r][c] == "#":
                return d
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] != "X":
                    seen.add((nr, nc))
                    queue.append((nr, nc, d + 1))
        return -1
