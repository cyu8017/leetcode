# LeetCode 2258 - Escape the Spreading Fire
# https://leetcode.com/problems/escape-the-spreading-fire/

from collections import deque
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        inf = 1000000000
        fire = [[inf] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fire[i][j] = 0
                    q.append((i, j))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 2 or fire[nr][nc] != inf:
                    continue
                fire[nr][nc] = fire[r][c] + 1
                q.append((nr, nc))

        def can(wait: int) -> bool:
            if wait >= fire[0][0]:
                return False
            vis = [[False] * n for _ in range(m)]
            qq = deque([(0, 0, wait)])
            vis[0][0] = True
            while qq:
                r, c, t = qq.popleft()
                for dr, dc in dirs:
                    nr, nc, nt = r + dr, c + dc, t + 1
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 2 or vis[nr][nc]:
                        continue
                    if nr == m - 1 and nc == n - 1:
                        if nt <= fire[nr][nc]:
                            return True
                        continue
                    if nt >= fire[nr][nc]:
                        continue
                    vis[nr][nc] = True
                    qq.append((nr, nc, nt))
            return False

        lo, hi, ans = 0, m * n + 10, -1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        if ans >= m * n:
            return inf
        return ans
