# LeetCode 3383 - Minimum Runes to Add to Cast Spell
# https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

from typing import List


class Solution:
    def minRunesToAdd(
        self, n: int, crystals: List[int], flowFrom: List[int], flowTo: List[int]
    ) -> int:
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        for i in range(len(flowFrom)):
            a, b = flowFrom[i], flowTo[i]
            g[a].append(b)
            rg[b].append(a)
        vis = [False] * n
        order = []

        def dfs1(u: int) -> None:
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    dfs1(v)
            order.append(u)

        for i in range(n):
            if not vis[i]:
                dfs1(i)
        comp = [-1] * n
        cid = 0

        def dfs2(u: int) -> None:
            comp[u] = cid
            for v in rg[u]:
                if comp[v] == -1:
                    dfs2(v)

        for i in range(n - 1, -1, -1):
            u = order[i]
            if comp[u] == -1:
                dfs2(u)
                cid += 1
        has_crystal = [False] * cid
        for c in crystals:
            has_crystal[comp[c]] = True
        indeg = [0] * cid
        for u in range(n):
            for v in g[u]:
                if comp[u] != comp[v]:
                    indeg[comp[v]] += 1
        ans = 0
        for i in range(cid):
            if indeg[i] == 0 and not has_crystal[i]:
                ans += 1
        return ans
