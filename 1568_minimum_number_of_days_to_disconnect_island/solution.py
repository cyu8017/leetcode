from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def islands():
            seen, count = set(), 0
            for r in range(m):
                for c in range(n):
                    if grid[r][c] and (r, c) not in seen:
                        count += 1
                        stack = [(r, c)]
                        seen.add((r, c))
                        while stack:
                            x, y = stack.pop()
                            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] and (nx, ny) not in seen:
                                    seen.add((nx, ny)); stack.append((nx, ny))
            return count
        if islands() != 1:
            return 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    grid[r][c] = 0
                    if islands() != 1:
                        grid[r][c] = 1
                        return 1
                    grid[r][c] = 1
        return 2
