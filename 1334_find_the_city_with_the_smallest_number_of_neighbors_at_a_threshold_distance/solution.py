# LeetCode 1334 - Find The City With The Smallest Number Of Neighbors At A Threshold Distance

from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf = 10**15
        dist = [[inf] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for a, b, weight in edges:
            dist[a][b] = dist[b][a] = weight
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return min(range(n), key=lambda city: (sum(d <= distanceThreshold for d in dist[city]), -city))
