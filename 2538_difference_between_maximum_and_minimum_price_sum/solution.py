# LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
# https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

from typing import List


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        ans = [0]

        def dfs(u: int, p: int) -> int:
            max_child = 0
            for v in g[u]:
                if v == p:
                    continue
                child = dfs(v, u)
                if child > max_child:
                    max_child = child
                if child > ans[0]:
                    ans[0] = child
            return price[u] + max_child

        dfs(0, -1)
        return ans[0]
