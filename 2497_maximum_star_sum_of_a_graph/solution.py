# LeetCode 2497 - Maximum Star Sum of a Graph
# https://leetcode.com/problems/maximum-star-sum-of-a-graph/

from typing import List


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = vals[0]
        for i in range(n):
            neigh = []
            for v in g[i]:
                if vals[v] > 0:
                    neigh.append(vals[v])
            neigh.sort(reverse=True)
            s = vals[i]
            for j in range(min(len(neigh), k)):
                s += neigh[j]
            if s > ans:
                ans = s
        return ans
