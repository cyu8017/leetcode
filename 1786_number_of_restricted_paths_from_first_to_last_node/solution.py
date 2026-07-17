import heapq
from functools import lru_cache

class Solution:
    def countRestrictedPaths(self, n, edges):
        adj = [[] for _ in range(n + 1)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))
        dist = [float("inf")] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        MOD = 1_000_000_007

        @lru_cache(None)
        def dfs(u):
            if u == n:
                return 1
            total = 0
            for v, _ in adj[u]:
                if dist[u] > dist[v]:
                    total = (total + dfs(v)) % MOD
            return total

        return dfs(1)
