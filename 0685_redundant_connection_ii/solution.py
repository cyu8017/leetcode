# LeetCode 0685 - Redundant Connection II
# https://leetcode.com/problems/redundant-connection-ii/

from typing import List, Optional


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0] * (n + 1)
        cand1: Optional[List[int]] = None
        cand2: Optional[List[int]] = None

        for i, (u, v) in enumerate(edges):
            if parent[v] == 0:
                parent[v] = u
            else:
                cand1 = [parent[v], v]
                cand2 = [u, v]
                edges[i] = [-1, -1]
                break

        uf = list(range(n + 1))

        def find(x: int) -> int:
            while uf[x] != x:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        for u, v in edges:
            if u < 0:
                continue
            pu, pv = find(u), find(v)
            if pu == pv:
                return cand1 if cand1 is not None else [u, v]
            uf[pu] = pv

        return cand2 if cand2 is not None else []
