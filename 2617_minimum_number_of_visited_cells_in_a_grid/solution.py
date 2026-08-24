# LeetCode 2617 - Minimum Number of Visited Cells in a Grid
# https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

from collections import deque
from typing import List


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[-1] * n for _ in range(m)]
        q = deque([(0, 0)])
        dist[0][0] = 1
        while q:
            r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                return dist[r][c]
            nc = c + 1
            while nc <= c + grid[r][c] and nc < n:
                if dist[r][nc] == -1:
                    dist[r][nc] = dist[r][c] + 1
                    q.append((r, nc))
                nc += 1
            nr = r + 1
            while nr <= r + grid[r][c] and nr < m:
                if dist[nr][c] == -1:
                    dist[nr][c] = dist[r][c] + 1
                    q.append((nr, c))
                nr += 1
        return -1
