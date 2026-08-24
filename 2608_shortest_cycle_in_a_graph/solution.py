# LeetCode 2608 - Shortest Cycle in a Graph
# https://leetcode.com/problems/shortest-cycle-in-a-graph/

from collections import deque
from typing import List


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        INF = 1000000000
        ans = INF
        for start in range(n):
            dist = [-1] * n
            parent = [-1] * n
            q = deque([start])
            dist[start] = 0
            while q:
                u = q.popleft()
                for v in g[u]:
                    if dist[v] < 0:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:
                        c = dist[u] + dist[v] + 1
                        if c < ans:
                            ans = c
        return -1 if ans == INF else ans
