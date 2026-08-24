# LeetCode 2925 - Maximum Score After Applying Operations on a Tree
# https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

from typing import List


class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        total = sum(values)

        def dfs(u: int, p: int) -> int:
            sum_kids = 0
            is_leaf = True
            for v in g[u]:
                if v == p:
                    continue
                is_leaf = False
                sum_kids += dfs(v, u)
            if is_leaf:
                return values[u]
            return values[u] if values[u] < sum_kids else sum_kids

        return total - dfs(0, -1)
