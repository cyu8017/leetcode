# LeetCode 2093 - Minimum Cost to Reach City With Discounts
# https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

import heapq
from typing import List


class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        g = [[] for _ in range(n)]
        for a, b, c in highways:
            g[a].append((b, c))
            g[b].append((a, c))
        INF = 1 << 30
        dist = [[INF] * (discounts + 1) for _ in range(n)]
        dist[0][discounts] = 0
        pq = [(0, 0, discounts)]
        while pq:
            cost, city, disc = heapq.heappop(pq)
            if city == n - 1:
                return cost
            if cost > dist[city][disc]:
                continue
            for v, w in g[city]:
                if cost + w < dist[v][disc]:
                    dist[v][disc] = cost + w
                    heapq.heappush(pq, (dist[v][disc], v, disc))
                if disc > 0 and cost + w // 2 < dist[v][disc - 1]:
                    dist[v][disc - 1] = cost + w // 2
                    heapq.heappush(pq, (dist[v][disc - 1], v, disc - 1))
        return -1
