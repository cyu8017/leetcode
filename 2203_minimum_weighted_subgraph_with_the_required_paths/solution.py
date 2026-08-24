# LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

from typing import List
class MinHeap:
    def __init__(self, cmp):
        self.a = []
        self.cmp = cmp or (lambda x, y: x - y)

    def _up(self, i):
        a = self.a
        cmp = self.cmp
        while i > 0:
            p = (i - 1) >> 1
            if cmp(a[i], a[p]) >= 0:
                break
            a[i], a[p] = a[p], a[i]
            i = p

    def _down(self, i):
        a = self.a
        cmp = self.cmp
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

    def push(self, x):
        self.a.append(x)
        self._up(len(self.a) - 1)

    def pop(self):
        a = self.a
        if not len(a):
            return None
        top = a[0]
        last = a.pop()
        if a:
            a[0] = last
            self._down(0)
        return top

    def peek(self):
        return self.a[0]

    def size(self):
        return len(self.a)

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        INF = 2 ** 53 - 1
        def dijkstra(g, src):
            dist = [INF] * (n)
            dist[src] = 0
            pq = MinHeap(lambda a, b: a[0] - b[0])
            pq.push([0, src])
            while pq.size():
                d, u = pq.pop()
                if d != dist[u]:
                    continue
                for v, w in g[u]:
                    if d + w < dist[v]:
                        dist[v] = d + w
                        pq.push([dist[v], v])
            return dist

        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append([e[1], e[2]])
            rg[e[1]].append([e[0], e[2]])
        d1 = dijkstra(g, src1)
        d2 = dijkstra(g, src2)
        dd = dijkstra(rg, dest)
        ans = INF
        for i in range(n):
            if d1[i] >= INF or d2[i] >= INF or dd[i] >= INF:
                continue
            ans = min(ans, d1[i] + d2[i] + dd[i])
        return -1 if ans >= INF else ans
