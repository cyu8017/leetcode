# LeetCode 2277 - Closest Node to Path in Tree
# https://leetcode.com/problems/closest-node-to-path-in-tree/

from typing import List


class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        LOG = 17
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n

        def dfs(u: int, p: int) -> None:
            up[0][u] = p
            for v in g[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)

        dfs(0, 0)
        for k in range(1, LOG):
            for v in range(n):
                up[k][v] = up[k - 1][up[k - 1][v]]

        def lift(v: int, d: int) -> int:
            for k in range(LOG):
                if (d >> k) & 1:
                    v = up[k][v]
            return v

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            a = lift(a, depth[a] - depth[b])
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return up[0][a]

        def dist(a: int, b: int) -> int:
            c = lca(a, b)
            return depth[a] + depth[b] - 2 * depth[c]

        ans = [0] * len(query)
        for i, (a, b, x) in enumerate(query):
            cands = [lca(a, b), lca(a, x), lca(b, x)]
            best = cands[0]
            best_d = dist(cands[0], x)
            for t in range(1, 3):
                d = dist(cands[t], x)
                if d < best_d:
                    best_d = d
                    best = cands[t]
            ans[i] = best
        return ans
