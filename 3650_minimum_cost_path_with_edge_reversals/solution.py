# LeetCode 3650 - Minimum Cost Path with Edge Reversals
# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

from typing import List
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w * 2))
        inf = 1073741823
        dist = [inf] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == n - 1:
                return d
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return -1
