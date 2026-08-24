# LeetCode 4003 - Minimum Cost Path with Alternating Directions III
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

from typing import List
import heapq


class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        INF = 2 ** 60
        dist = [[[INF, INF] for _ in range(n)] for _ in range(m)]
        dist[0][0][1] = 1
        pq = [[1, 0, 0, 1]]
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        while pq:
            cur = heapq.heappop(pq)
            d, i, j, k = cur[0], cur[1], cur[2], cur[3]
            if i == m - 1 and j == n - 1:
                return d
            if d > dist[i][j][k]:
                continue
            p = penalty[i][j]
            nd = d + p
            if nd < dist[i][j][k ^ 1]:
                dist[i][j][k ^ 1] = nd
                heapq.heappush(pq, [nd, i, j, k ^ 1])
            for idx in range(4):
                x = i + dirs[idx][0]
                y = j + dirs[idx][1]
                if 0 <= x < m and 0 <= y < n:
                    nd = d + ((x + 1) * (y + 1) + (((idx & 1) ^ k) * p))
                    if nd < dist[x][y][k ^ 1]:
                        dist[x][y][k ^ 1] = nd
                        heapq.heappush(pq, [nd, x, y, k ^ 1])
        return -1
