# LeetCode 3286 - Find a Safe Walk Through a Grid
# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

from collections import deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        vis = [[-1] * n for _ in range(m)]
        qh = health - grid[0][0]
        if qh <= 0:
            return False
        q = deque([[0, 0, qh]])
        vis[0][0] = qh
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            cur = q.popleft()
            if cur[0] == m - 1 and cur[1] == n - 1:
                return True
            for d in dirs:
                nr, nc = cur[0] + d[0], cur[1] + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                nh = cur[2] - grid[nr][nc]
                if nh <= 0:
                    continue
                if nh > vis[nr][nc]:
                    vis[nr][nc] = nh
                    q.append([nr, nc, nh])
        return False
