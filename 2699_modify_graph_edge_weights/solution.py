# LeetCode 2699 - Modify Graph Edge Weights
# https://leetcode.com/problems/modify-graph-edge-weights/

import heapq
from typing import List


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        INF = 2000000000

        def dijkstra(ignore_neg: bool) -> List[int]:
            dist = [INF] * n
            dist[source] = 0
            pq = [(0, source)]
            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for e in edges:
                    a, b, w = e[0], e[1], e[2]
                    if a != u and b != u:
                        continue
                    to = b if a == u else a
                    if w == -1:
                        if ignore_neg:
                            continue
                        w = 1
                    if d + w < dist[to]:
                        dist[to] = d + w
                        heapq.heappush(pq, (dist[to], to))
            return dist

        d = dijkstra(True)
        if d[destination] < target:
            return []
        matched = d[destination] == target
        for i in range(len(edges)):
            if edges[i][2] != -1:
                continue
            if matched:
                edges[i][2] = INF
                continue
            edges[i][2] = 1
            d = dijkstra(False)
            if d[destination] <= target:
                edges[i][2] += target - d[destination]
                matched = True
        d = dijkstra(False)
        if d[destination] != target:
            return []
        return edges
