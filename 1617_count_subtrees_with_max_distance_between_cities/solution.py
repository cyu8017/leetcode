class Solution:
    def countSubgraphsForEachDiameter(self, n, edges):
        adj = [[] for _ in range(n)]
        for a, b in edges: a -= 1; b -= 1; adj[a].append(b); adj[b].append(a)
        ans = [0] * (n - 1)
        for mask in range(1, 1 << n):
            if mask & (mask - 1) == 0: continue
            start = (mask & -mask).bit_length() - 1
            def bfs(src):
                dist = {src: 0}; q = [src]
                for u in q:
                    for v in adj[u]:
                        if mask >> v & 1 and v not in dist: dist[v] = dist[u] + 1; q.append(v)
                far = max(dist, key=dist.get)
                return far, dist
            far, seen = bfs(start)
            if len(seen) == mask.bit_count():
                _, dist = bfs(far); ans[max(dist.values()) - 1] += 1
        return ans
