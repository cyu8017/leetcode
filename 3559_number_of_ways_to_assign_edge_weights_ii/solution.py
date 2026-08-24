# LeetCode 3559 - Number of Ways to Assign Edge Weights II
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

from typing import List


class Solution:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        MOD, LOG = 1000000007, 17
        n = len(edges) + 1
        depth = [0] * (n + 1)
        graph = [[] for _ in range(n + 1)]
        parent = [[-1] * (n + 1) for _ in range(LOG)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        def dfs(u: int, p: int) -> None:
            parent[0][u] = p
            for v in graph[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)

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

        def mod_pow(exp: int) -> int:
            base, res = 2, 1
            while exp > 0:
                if exp & 1:
                    res = res * base % MOD
                base = base * base % MOD
                exp >>= 1
            return res

        dfs(1, -1)
        for k in range(1, LOG):
            for v in range(1, n + 1):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            u, v = q[0], q[1]
            if u == v:
                ans[i] = 0
                continue
            a = lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[a]
            ans[i] = mod_pow(d - 1)
        return ans
