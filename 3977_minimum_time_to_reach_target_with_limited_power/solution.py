# LeetCode 3977 - Minimum Time to Reach Target With Limited Power
# https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

from typing import List
import heapq


class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        INF = 2 ** 62
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append([e[1], e[2]])
        dist = [[INF] * (power + 1) for _ in range(n)]
        pq = [[0, -power, source]]
        dist[source][power] = 0
        while pq:
            cur = heapq.heappop(pq)
            d, p, u = cur[0], -cur[1], cur[2]
            if u == target:
                return [d, p]
            if d > dist[u][p] or p < cost[u]:
                continue
            p -= cost[u]
            for e in g[u]:
                v, t = e[0], e[1]
                nd = d + t
                if nd < dist[v][p]:
                    dist[v][p] = nd
                    heapq.heappush(pq, [nd, -p, v])
        return [-1, -1]
