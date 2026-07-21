from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFee: List[int]) -> int:
        n = len(passingFee)
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # Dijkstra by cost; allow revisits only with strictly smaller time.
        min_time = [maxTime + 1] * n
        pq = [(passingFee[0], 0, 0)]  # cost, time, node
        while pq:
            cost, time, u = heapq.heappop(pq)
            if time >= min_time[u]:
                continue
            min_time[u] = time
            if u == n - 1:
                return cost
            for v, dt in graph[u]:
                nt = time + dt
                if nt <= maxTime and nt < min_time[v]:
                    heapq.heappush(pq, (cost + passingFee[v], nt, v))
        return -1
