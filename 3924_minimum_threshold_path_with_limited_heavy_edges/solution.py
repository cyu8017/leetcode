# LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
# https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

from typing import List


def can(n: int, g: List[List[List[int]]], source: int, target: int, k: int, threshold: int) -> bool:
    inf = 1000000000
    dist = [inf] * n
    dist[source] = 0
    dq: List[int] = [source]
    while dq:
        u = dq.pop(0)
        for e in g[u]:
            to, weight = e[0], e[1]
            cost = 1 if weight > threshold else 0
            if dist[u] + cost >= dist[to] or dist[u] + cost > k:
                continue
            dist[to] = dist[u] + cost
            if cost == 0:
                dq.insert(0, to)
            else:
                dq.append(to)
    return dist[target] <= k


class Solution:
    def minThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0
        g: List[List[List[int]]] = [[] for _ in range(n)]
        max_weight = 0
        for e in edges:
            g[e[0]].append([e[1], e[2]])
            g[e[1]].append([e[0], e[2]])
            max_weight = max(max_weight, e[2])
        if not can(n, g, source, target, k, max_weight):
            return -1
        lo = 0
        hi = max_weight
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if can(n, g, source, target, k, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
