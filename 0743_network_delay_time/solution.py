# LeetCode 0743 - Network Delay Time
# https://leetcode.com/problems/network-delay-time/

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n + 1)}
        dist[k] = 0
        heap = [(0, k)]
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for nei, weight in graph[node]:
                nd = d + weight
                if nd < dist[nei]:
                    dist[nei] = nd
                    heapq.heappush(heap, (nd, nei))

        ans = max(dist.values())
        return -1 if ans == float("inf") else int(ans)
