class Solution:
    def countRestrictedPaths(self, n, edges):
        import heapq
        adj = [[] for _ in range(n + 1)]
        for a, b, w in edges:
            adj[a].append((b, w)); adj[b].append((a, w))
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
        dp = [0] * (n + 1)
        dp[n] = 1
        for u in sorted(range(1, n + 1), key=lambda x: dist[x]):
            for v, _ in adj[u]:
                if dist[v] < dist[u]:
                    dp[v] = (dp[v] + dp[u]) % MOD
        return dp[1]
