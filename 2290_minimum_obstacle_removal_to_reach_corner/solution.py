# LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque([(0, 0)])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while dq:
            r, c = dq.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                nd = dist[r][c] + grid[nr][nc]
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    if grid[nr][nc] == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))
        return int(dist[m - 1][n - 1])
