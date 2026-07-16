from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = [sum(row) for row in grid]
        cols = [sum(grid[r][c] for r in range(len(grid))) for c in range(len(grid[0]))]
        return sum(grid[r][c] and (rows[r] > 1 or cols[c] > 1)
                   for r in range(len(grid)) for c in range(len(grid[0])))
