# LeetCode 3108 - Minimum Cost Walk in Weighted Graph
# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        p = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def unite(a: int, b: int) -> None:
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if size[pa] > size[pb]:
                p[pb] = pa
                size[pa] += size[pb]
            else:
                p[pa] = pb
                size[pb] += size[pa]

        g = [-1] * n
        for e in edges:
            unite(e[0], e[1])
        for e in edges:
            root = find(e[0])
            g[root] &= e[2]
        ans = [0] * len(query)
        for i, (u, v) in enumerate(query):
            if u == v:
                ans[i] = 0
            else:
                a, b = find(u), find(v)
                ans[i] = g[a] if a == b else -1
        return ans
