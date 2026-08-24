# LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

from typing import List


class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        LOG = 17
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        dist = [0] * n

        def dfs(u: int, p: int) -> None:
            parent[0][u] = p
            for to, w in g[u]:
                if to == p:
                    continue
                depth[to] = depth[u] + 1
                dist[to] = dist[u] + w
                dfs(to, u)

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and depth[parent[k][u]] >= depth[v]:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        def path(u: int, v: int) -> int:
            a = lca(u, v)
            return dist[u] + dist[v] - 2 * dist[a]

        dfs(0, -1)
        for k in range(1, LOG):
            for v in range(n):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            a, b, c = q[0], q[1], q[2]
            ans[i] = (path(a, b) + path(b, c) + path(a, c)) // 2
        return ans
