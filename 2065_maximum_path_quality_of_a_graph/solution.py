# LeetCode 2065 - Maximum Path Quality of a Graph
# https://leetcode.com/problems/maximum-path-quality-of-a-graph/

from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for u, v, t in edges:
            g[u].append((v, t))
            g[v].append((u, t))
        ans = 0
        vis = [0] * n

        def dfs(u: int, time: int, quality: int) -> None:
            nonlocal ans
            if time > maxTime:
                return
            first = vis[u] == 0
            if first:
                quality += values[u]
            vis[u] += 1
            if u == 0:
                ans = max(ans, quality)
            for v, w in g[u]:
                dfs(v, time + w, quality)
            vis[u] -= 1

        dfs(0, 0, 0)
        return ans
