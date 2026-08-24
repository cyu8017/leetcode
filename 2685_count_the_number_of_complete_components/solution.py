# LeetCode 2685 - Count the Number of Complete Components
# https://leetcode.com/problems/count-the-number-of-complete-components/

from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        vis = [False] * n
        ans = 0

        def dfs(u: int, nodes: List[int]) -> None:
            vis[u] = True
            nodes.append(u)
            for v in g[u]:
                if not vis[v]:
                    dfs(v, nodes)

        for i in range(n):
            if vis[i]:
                continue
            nodes = []
            dfs(i, nodes)
            ecount = 0
            for u in nodes:
                ecount += len(g[u])
            ecount //= 2
            sz = len(nodes)
            if ecount == sz * (sz - 1) // 2:
                ans += 1
        return ans
