# LeetCode 3552 - Grid Teleportation Traversal
# https://leetcode.com/problems/grid-teleportation-traversal/

from collections import deque
from typing import List


class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        g = {}
        for i in range(m):
            for j in range(n):
                c = matrix[i][j]
                if c.isalpha():
                    g.setdefault(c, []).append((i, j))
        dirs = [-1, 0, 1, 0, -1]
        INF = 1 << 30
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        while q:
            i, j = q.popleft()
            d = dist[i][j]
            if i == m - 1 and j == n - 1:
                return d
            c = matrix[i][j]
            if c in g:
                for x, y in g[c]:
                    if d < dist[x][y]:
                        dist[x][y] = d
                        q.appendleft((x, y))
                del g[c]
            for idx in range(4):
                x, y = i + dirs[idx], j + dirs[idx + 1]
                if 0 <= x < m and 0 <= y < n and matrix[x][y] != "#" and d + 1 < dist[x][y]:
                    dist[x][y] = d + 1
                    q.append((x, y))
        return -1
