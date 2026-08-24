# LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
# https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

from typing import Callable, List, Optional


class MinHeap:
    def __init__(self, cmp: Optional[Callable] = None):
        self.a = []
        self.cmp = cmp or (lambda x, y: x - y)

    def _up(self, i: int) -> None:
        a, cmp = self.a, self.cmp
        while i > 0:
            p = (i - 1) >> 1
            if cmp(a[i], a[p]) >= 0:
                break
            a[i], a[p] = a[p], a[i]
            i = p

    def _down(self, i: int) -> None:
        a, cmp = self.a, self.cmp
        n = len(a)
        while True:
            s = i
            l = i * 2 + 1
            r = l + 1
            if l < n and cmp(a[l], a[s]) < 0:
                s = l
            if r < n and cmp(a[r], a[s]) < 0:
                s = r
            if s == i:
                break
            a[i], a[s] = a[s], a[i]
            i = s

    def push(self, x) -> None:
        self.a.append(x)
        self._up(len(self.a) - 1)

    def pop(self):
        a = self.a
        if not a:
            return None
        top = a[0]
        last = a.pop()
        if a:
            a[0] = last
            self._down(0)
        return top

    def peek(self):
        return self.a[0]

    def size(self) -> int:
        return len(self.a)


class Solution:
    def minCostExcludingMax(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            u, v, w = e[0], e[1], e[2]
            g[u].append((v, w))
            g[v].append((u, w))
        INF = 10**18
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = 0
        pq = MinHeap(lambda a, b: a[0] - b[0])
        pq.push((0, 0, 0))
        while pq.size():
            c, u, used = pq.pop()
            if c > dist[u][used]:
                continue
            if u == n - 1 and used == 1:
                return c
            for v, w in g[u]:
                nxt = c + w
                if nxt < dist[v][used]:
                    dist[v][used] = nxt
                    pq.push((nxt, v, used))
                if used == 0:
                    nxt = c
                    if nxt < dist[v][1]:
                        dist[v][1] = nxt
                        pq.push((nxt, v, 1))
        return dist[n - 1][1]
