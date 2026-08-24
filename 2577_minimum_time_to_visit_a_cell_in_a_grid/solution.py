# LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

import heapq
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        m, n = len(grid), len(grid[0])
        dist = [[1 << 30] * n for _ in range(m)]
        h = [(0, 0, 0)]
        dist[0][0] = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while h:
            t, r, c = heapq.heappop(h)
            if r == m - 1 and c == n - 1:
                return t
            if t > dist[r][c]:
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                nt = t + 1
                if nt < grid[nr][nc]:
                    wait = grid[nr][nc] - nt
                    if wait % 2 == 1:
                        wait += 1
                    nt += wait
                if nt < dist[nr][nc]:
                    dist[nr][nc] = nt
                    heapq.heappush(h, (nt, nr, nc))
        return -1
