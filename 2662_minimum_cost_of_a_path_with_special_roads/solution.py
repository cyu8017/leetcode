# LeetCode 2662 - Minimum Cost of a Path With Special Roads
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

import heapq
from typing import List


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        points = [start, target]
        for r in specialRoads:
            points.append([r[0], r[1]])
            points.append([r[2], r[3]])
        N = len(points)

        def man(a: List[int], b: List[int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        g = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j:
                    g[i].append((j, man(points[i], points[j])))
        for r in specialRoads:
            u = v = -1
            for i, p in enumerate(points):
                if p[0] == r[0] and p[1] == r[1]:
                    u = i
                if p[0] == r[2] and p[1] == r[3]:
                    v = i
            if u >= 0 and v >= 0:
                g[u].append((v, r[4]))
        dist = [10**18] * N
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            cost, idx = heapq.heappop(pq)
            if cost > dist[idx]:
                continue
            for to, w in g[idx]:
                if cost + w < dist[to]:
                    dist[to] = cost + w
                    heapq.heappush(pq, (dist[to], to))
        return dist[1]
