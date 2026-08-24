# LeetCode 3887 - Incremental Even-Weighted Cycle Queries
# https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

from typing import List, Tuple


class Solution:
    def countValidEdges(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        parity = [0] * n

        def find(x: int) -> Tuple[int, int]:
            if parent[x] == x:
                return (x, 0)
            res = find(parent[x])
            root, p = res[0], res[1]
            parity[x] ^= p
            parent[x] = root
            return (root, parity[x])

        ans = 0
        for e in edges:
            fu = find(e[0])
            fv = find(e[1])
            ru, pu = fu[0], fu[1]
            rv, pv = fv[0], fv[1]
            if ru == rv:
                if (pu ^ pv) == e[2]:
                    ans += 1
                continue
            if size[ru] < size[rv]:
                ru, rv = rv, ru
                pu, pv = pv, pu
            parent[rv] = ru
            parity[rv] = pu ^ pv ^ e[2]
            size[ru] += size[rv]
            ans += 1
        return ans
