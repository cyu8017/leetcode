# LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
# https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

import heapq
from typing import List


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        INF = 1 << 30
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            du, u = heapq.heappop(pq)
            if du > dist[u]:
                continue
            for v, w in g[u]:
                if dist[v] > dist[u] + w and dist[u] + w < disappear[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return [dist[i] if dist[i] < disappear[i] else -1 for i in range(n)]
