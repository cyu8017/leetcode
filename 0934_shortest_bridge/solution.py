# LeetCode 0934 - Shortest Bridge
# https://leetcode.com/problems/shortest-bridge/

from collections import deque


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def find_start() -> tuple[int, int]:
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        return i, j
            return 0, 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return
            grid[r][c] = 2
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        sr, sc = find_start()
        dfs(sr, sc)
        queue = deque((i, j, 0) for i in range(n) for j in range(n) if grid[i][j] == 2)
        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == 1:
                        return dist
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        queue.append((nr, nc, dist + 1))
        return -1
