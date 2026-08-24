# LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
# https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

from typing import List


class Solution:
    def minimumSeconds(self, land: List[List[str]]) -> int:
        m, n = len(land), len(land[0])
        INF = 10**9
        water = [[INF] * n for _ in range(m)]
        wq = []
        sx = sy = dx = dy = 0
        for i in range(m):
            for j in range(n):
                cell = land[i][j]
                if cell == "*":
                    water[i][j] = 0
                    wq.append((i, j))
                elif cell == "S":
                    sx, sy = i, j
                elif cell == "D":
                    dx, dy = i, j
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        h = 0
        while h < len(wq):
            x, y = wq[h]
            h += 1
            for ddx, ddy in dirs:
                ni, nj = x + ddx, y + ddy
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue
                cell = land[ni][nj]
                if cell in ("X", "D"):
                    continue
                if water[ni][nj] > water[x][y] + 1:
                    water[ni][nj] = water[x][y] + 1
                    wq.append((ni, nj))
        dist = [[-1] * n for _ in range(m)]
        q = [(sx, sy)]
        dist[sx][sy] = 0
        h = 0
        while h < len(q):
            x, y = q[h]
            h += 1
            if x == dx and y == dy:
                return dist[x][y]
            for ddx, ddy in dirs:
                ni, nj = x + ddx, y + ddy
                if ni < 0 or nj < 0 or ni >= m or nj >= n or dist[ni][nj] != -1:
                    continue
                if land[ni][nj] == "X":
                    continue
                nd = dist[x][y] + 1
                if land[ni][nj] != "D" and nd >= water[ni][nj]:
                    continue
                dist[ni][nj] = nd
                q.append((ni, nj))
        return -1
