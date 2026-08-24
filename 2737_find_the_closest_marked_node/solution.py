# LeetCode 2737 - Find the Closest Marked Node
# https://leetcode.com/problems/find-the-closest-marked-node/

import heapq
from typing import List


class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
        mark = set(marked)
        dist = [10**18] * n
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if u in mark:
                return d
            if d > dist[u]:
                continue
            for v, w in g[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        return -1
