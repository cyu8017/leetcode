# LeetCode 2473 - Minimum Cost to Buy Apples
# https://leetcode.com/problems/minimum-cost-to-buy-apples/

import heapq
from typing import List


class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        g = [[] for _ in range(n + 1)]
        for r in roads:
            g[r[0]].append((r[1], r[2]))
            g[r[1]].append((r[0], r[2]))
        ans = [0] * n
        INF = 10**18
        for start in range(1, n + 1):
            dist = [INF] * (n + 1)
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for v, w in g[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            best = INF
            for city in range(1, n + 1):
                cost = dist[city] * (k + 1) + appleCost[city - 1]
                if cost < best:
                    best = cost
            ans[start - 1] = best
        return ans
