# LeetCode 2307 - Check for Contradictions in Equations
# https://leetcode.com/problems/check-for-contradictions-in-equations/

from typing import List


class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        parent = {}
        weight = {}

        def find(x: str) -> str:
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0
                return x
            if parent[x] != x:
                old = parent[x]
                p = find(old)
                weight[x] = weight[x] * weight[old]
                parent[x] = p
            return parent[x]

        for i, (a, b) in enumerate(equations):
            ra, rb = find(a), find(b)
            if ra == rb:
                if abs(weight[a] / weight[b] - values[i]) > 1e-5:
                    return True
            else:
                parent[ra] = rb
                weight[ra] = values[i] * weight[b] / weight[a]
        return False
