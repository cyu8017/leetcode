class Solution:
    def minTrioDegree(self, n, edges):
        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a - 1].add(b - 1); adj[b - 1].add(a - 1)
        best = float("inf")
        for i in range(n):
            for j in adj[i]:
                if j <= i:
                    continue
                for k in adj[i]:
                    if k <= j or k not in adj[j]:
                        continue
                    best = min(best, len(adj[i]) + len(adj[j]) + len(adj[k]) - 6)
        return -1 if best == float("inf") else best
