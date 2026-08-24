# LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
# https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2], e[3]))
        Inf = 10**18
        dist = [Inf] * n
        dist[0] = 0
        pq = [[0, 0]]

        def push(t: int, u: int) -> None:
            lo, hi = 0, len(pq)
            while lo < hi:
                mid = (lo + hi) >> 1
                if pq[mid][0] < t:
                    lo = mid + 1
                else:
                    hi = mid
            pq.insert(lo, [t, u])

        while pq:
            t, u = pq.pop(0)
            if t != dist[u]:
                continue
            if u == n - 1:
                return t
            for to, start, end in g[u]:
                nt = t
                if nt > end:
                    continue
                if nt < start:
                    nt = start
                nt += 1
                if nt < dist[to]:
                    dist[to] = nt
                    push(nt, to)
        return -1 if dist[n - 1] == Inf else dist[n - 1]
