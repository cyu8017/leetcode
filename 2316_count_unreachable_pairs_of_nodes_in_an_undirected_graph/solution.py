# LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        vis = [False] * n

        def dfs(u: int) -> int:
            vis[u] = True
            size = 1
            for v in g[u]:
                if not vis[v]:
                    size += dfs(v)
            return size

        ans = seen = 0
        for i in range(n):
            if not vis[i]:
                sz = dfs(i)
                ans += sz * seen
                seen += sz
        return ans
