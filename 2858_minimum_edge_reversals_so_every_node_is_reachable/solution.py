# LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
# https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

from typing import List


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append((v, 0))
            g[v].append((u, 1))
        ans = [0] * n

        def dfs1(u: int, p: int) -> None:
            for v, ww in g[u]:
                if v == p:
                    continue
                ans[0] += ww
                dfs1(v, u)

        def dfs2(u: int, p: int) -> None:
            for v, ww in g[u]:
                if v == p:
                    continue
                ans[v] = ans[u] + 1 if ww == 0 else ans[u] - 1
                dfs2(v, u)

        dfs1(0, -1)
        dfs2(0, -1)
        return ans
