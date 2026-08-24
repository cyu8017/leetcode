# LeetCode 2503 - Maximum Number of Points From Grid Queries
# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

import heapq
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        order = list(range(len(queries)))
        order.sort(key=lambda i: queries[i])
        ans = [0] * len(queries)
        visited = [[False] * n for _ in range(m)]
        pq = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        points = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for qi in order:
            q = queries[qi]
            while pq and pq[0][0] < q:
                _, r, c = heapq.heappop(pq)
                points += 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heapq.heappush(pq, (grid[nr][nc], nr, nc))
            ans[qi] = points
        return ans
