# LeetCode 3311 - Construct 2D Grid Matching Graph Layout
# https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

from typing import List


class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        deg = [len(g[i]) for i in range(n)]
        start = 0
        for i in range(n):
            if deg[i] == 1:
                start = i
                break
            if deg[i] == 2:
                start = i
        vis = [False] * n
        row = []
        cur, prev = start, -1
        while True:
            row.append(cur)
            vis[cur] = True
            nxt = -1
            for v in g[cur]:
                if v != prev and (not vis[v]) and deg[v] <= 3:
                    nxt = v
                    if deg[v] < 4:
                        break
            if nxt == -1:
                break
            prev = cur
            cur = nxt
        width = len(row)
        height = n // width if width != 0 else n
        if width == 0 or width * height != n:
            for w in range(1, n + 1):
                if n % w == 0:
                    width = w
                    height = n // w
                    break
        grid = [[0] * width for _ in range(height)]
        for i in range(n):
            grid[i // width][i % width] = i
        return grid
