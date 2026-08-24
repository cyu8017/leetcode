# LeetCode 3772 - Maximum Subgraph Score in a Tree
# https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

from typing import List


class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        parent = [-2] * n
        parent[0] = -1
        order = [0]
        i = 0
        while i < len(order):
            u = order[i]
            for v in g[u]:
                if parent[v] == -2:
                    parent[v] = u
                    order.append(v)
            i += 1
        down = [0] * n
        for i in range(n - 1, -1, -1):
            u = order[i]
            down[u] = 2 * good[u] - 1
            for v in g[u]:
                if parent[v] == u and down[v] > 0:
                    down[u] += down[v]
        ans = down[:]
        for u in order:
            for v in g[u]:
                if parent[v] == u:
                    outside = ans[u]
                    if down[v] > 0:
                        outside -= down[v]
                    ans[v] = down[v]
                    if outside > 0:
                        ans[v] += outside
        return ans
