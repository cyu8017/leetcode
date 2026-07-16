# LeetCode 0684 - Redundant Connection
# https://leetcode.com/problems/redundant-connection/

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return [u, v]
            parent[pu] = pv
        return []
