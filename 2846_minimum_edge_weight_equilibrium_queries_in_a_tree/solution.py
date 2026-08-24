# LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
# https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

from typing import List


class Solution:
    def minOperationsQueries(
        self, n: int, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        LOG = 15
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append((b, w))
            g[b].append((a, w))
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        cnt = [[0] * 27 for _ in range(n)]

        def dfs(u: int, p: int) -> None:
            up[0][u] = p
            for v, w in g[u]:
                if v == p:
                    continue
                depth[v] = depth[u] + 1
                for i in range(27):
                    cnt[v][i] = cnt[u][i]
                cnt[v][w] += 1
                dfs(v, u)

        dfs(0, 0)
        for j in range(1, LOG):
            for i in range(n):
                up[j][i] = up[j - 1][up[j - 1][i]]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for j in range(LOG):
                if diff & (1 << j):
                    a = up[j][a]
            if a == b:
                return a
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]
            return up[0][a]

        out = []
        for a, b in queries:
            c = lca(a, b)
            total = depth[a] + depth[b] - 2 * depth[c]
            best = 0
            for w in range(1, 27):
                f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w]
                if f > best:
                    best = f
            out.append(total - best)
        return out
