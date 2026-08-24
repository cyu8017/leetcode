# LeetCode 2714 - Find Shortest Path With K Hops
# https://leetcode.com/problems/find-shortest-path-with-k-hops/

import heapq
from typing import List


class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        INF = 10**18
        dist = [[INF] * (k + 1) for _ in range(n)]
        dist[s][0] = 0
        pq = [(0, s, 0)]
        while pq:
            cd, u, hops = heapq.heappop(pq)
            if u == d:
                return cd
            if cd > dist[u][hops]:
                continue
            for to, w in g[u]:
                if cd + w < dist[to][hops]:
                    dist[to][hops] = cd + w
                    heapq.heappush(pq, (dist[to][hops], to, hops))
                if hops < k and cd < dist[to][hops + 1]:
                    dist[to][hops + 1] = cd
                    heapq.heappush(pq, (cd, to, hops + 1))
        return -1
