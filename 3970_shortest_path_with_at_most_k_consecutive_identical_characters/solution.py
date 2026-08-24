# LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

from typing import List
import heapq


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append([edge[1], edge[2]])
        infinity = (1 << 53) // 4
        distances = [[infinity] * (k + 1) for _ in range(n)]
        distances[0][1] = 0
        pq = [[0, 0, 1]]
        while pq:
            cur = heapq.heappop(pq)
            distance, node, run = cur[0], cur[1], cur[2]
            if distance != distances[node][run]:
                continue
            if node == n - 1:
                return distance
            for e in graph[node]:
                to, weight = e[0], e[1]
                next_run = 1
                if labels[node] == labels[to]:
                    next_run = run + 1
                if next_run > k:
                    continue
                next_distance = distance + weight
                if next_distance < distances[to][next_run]:
                    distances[to][next_run] = next_distance
                    heapq.heappush(pq, [next_distance, to, next_run])
        return -1
