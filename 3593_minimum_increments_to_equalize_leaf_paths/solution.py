# LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
# https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

from typing import List


class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        ans = 0

        def dfs(u: int, p: int) -> int:
            nonlocal ans
            if len(graph[u]) == 1 and p != -1:
                return cost[u]
            child_vals = []
            for v in graph[u]:
                if v == p:
                    continue
                child_vals.append(dfs(v, u))
            if not child_vals:
                return cost[u]
            mx = max(child_vals)
            for c in child_vals:
                if c < mx:
                    ans += 1
            return mx + cost[u]

        dfs(0, -1)
        return ans
