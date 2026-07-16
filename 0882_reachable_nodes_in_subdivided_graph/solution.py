# LeetCode 0882 - Reachable Nodes In Subdivided Graph
# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

import heapq
from collections import defaultdict


class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = graph[v][u] = cnt
        pq = [(-maxMoves, 0)]
        seen: dict[int, int] = {}
        while pq:
            moves, node = heapq.heappop(pq)
            moves = -moves
            if node in seen:
                continue
            seen[node] = moves
            for nei, cnt in graph[node].items():
                remain = moves - cnt - 1
                if nei not in seen and remain >= 0:
                    heapq.heappush(pq, (-remain, nei))
        ans = len(seen)
        for u, v, cnt in edges:
            ans += min(cnt, seen.get(u, 0) + seen.get(v, 0))
        return ans
