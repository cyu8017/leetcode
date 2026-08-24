# LeetCode 3613 - Minimize Maximum Component Cost
# https://leetcode.com/problems/minimize-maximum-component-cost/

from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        p = list(range(n))

        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        if k == n:
            return 0
        edges.sort(key=lambda e: e[2])
        cnt = n
        for e in edges:
            pu, pv = find(e[0]), find(e[1])
            if pu != pv:
                p[pu] = pv
                cnt -= 1
                if cnt <= k:
                    return e[2]
        return 0
