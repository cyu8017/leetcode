# LeetCode 2392 - Build a Matrix With Conditions
# https://leetcode.com/problems/build-a-matrix-with-conditions/

from typing import List, Optional


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        def topo(conds: List[List[int]]) -> Optional[List[int]]:
            g = [[] for _ in range(k + 1)]
            indeg = [0] * (k + 1)
            for c in conds:
                g[c[0]].append(c[1])
                indeg[c[1]] += 1
            q = [i for i in range(1, k + 1) if indeg[i] == 0]
            order = []
            while q:
                u = q.pop(0)
                order.append(u)
                for v in g[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
            if len(order) != k:
                return None
            return order

        row_order = topo(rowConditions)
        col_order = topo(colConditions)
        if not row_order or not col_order:
            return []
        row_pos = [0] * (k + 1)
        col_pos = [0] * (k + 1)
        for i in range(k):
            row_pos[row_order[i]] = i
            col_pos[col_order[i]] = i
        ans = [[0] * k for _ in range(k)]
        for v in range(1, k + 1):
            ans[row_pos[v]][col_pos[v]] = v
        return ans
