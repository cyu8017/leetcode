# LeetCode 2378 - Choose Edges to Maximize Score in a Tree
# https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

from typing import List


class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        n = len(edges)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            p, w = edges[i][0], edges[i][1]
            g[p].append((i, w))

        def dfs(u: int):
            base = 0
            best_gain = 0
            for to, w in g[u]:
                child = dfs(to)
                base += child[0]
                gain = child[1] + w - child[0]
                if gain > best_gain:
                    best_gain = gain
            return (base + best_gain, base)

        return dfs(0)[0]
