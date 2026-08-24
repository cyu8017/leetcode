# LeetCode 3543 - Maximum Weighted K-Edge Path
# https://leetcode.com/problems/maximum-weighted-k-edge-path/

from typing import List


class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append((e[1], e[2]))
        dp = [[set() for _ in range(k + 1)] for _ in range(n)]
        for u in range(n):
            dp[u][0].add(0)
        for i in range(k):
            for u in range(n):
                for sm in dp[u][i]:
                    for to, w in graph[u]:
                        ns = sm + w
                        if ns < t:
                            dp[to][i + 1].add(ns)
        ans = -1
        for u in range(n):
            for sm in dp[u][k]:
                if sm > ans:
                    ans = sm
        return ans
