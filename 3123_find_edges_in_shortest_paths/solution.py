# LeetCode 3123 - Find Edges in Shortest Paths
# https://leetcode.com/problems/find-edges-in-shortest-paths/

import heapq
from collections import deque
from typing import List


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for i, (a, b, w) in enumerate(edges):
            g[a].append((b, w, i))
            g[b].append((a, w, i))
        INF = 1 << 30
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            da, a = heapq.heappop(pq)
            if da > dist[a]:
                continue
            for b, w, _ in g[a]:
                if dist[b] > dist[a] + w:
                    dist[b] = dist[a] + w
                    heapq.heappush(pq, (dist[b], b))
        ans = [False] * len(edges)
        if dist[n - 1] == INF:
            return ans
        q = deque([n - 1])
        while q:
            a = q.popleft()
            for b, w, i in g[a]:
                if dist[a] == dist[b] + w:
                    ans[i] = True
                    q.append(b)
        return ans
