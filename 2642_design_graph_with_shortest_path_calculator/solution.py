# LeetCode 2642 - Design Graph With Shortest Path Calculator
# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

import heapq
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.g = [[] for _ in range(n)]
        for e in edges:
            self.g[e[0]].append((e[1], e[2]))

    def addEdge(self, edge: List[int]) -> None:
        self.g[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.g)
        dist = [1 << 30] * n
        dist[node1] = 0
        pq = [(0, node1)]
        while pq:
            d, u = heapq.heappop(pq)
            if u == node2:
                return d
            if d > dist[u]:
                continue
            for v, w in self.g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return -1
