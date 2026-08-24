# LeetCode 3558 - Number of Ways to Assign Edge Weights I
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 1000000007
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        def dfs(i: int, fa: int) -> int:
            res = 0
            for j in g[i]:
                if j != fa:
                    res = max(res, dfs(j, i) + 1)
            return res

        def pow2(exp: int) -> int:
            a, res = 2, 1
            while exp > 0:
                if exp & 1:
                    res = res * a % mod
                a = a * a % mod
                exp >>= 1
            return res

        return pow2(dfs(1, 0) - 1)
