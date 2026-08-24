# LeetCode 3608 - Minimum Time for K Connected Components
# https://leetcode.com/problems/minimum-time-for-k-connected-components/

from typing import List


class UnionFind3608:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def unite(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True


class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges = sorted(edges, key=lambda e: e[2])
        uf = UnionFind3608(n)
        cnt = n
        for i in range(len(edges) - 1, -1, -1):
            if uf.unite(edges[i][0], edges[i][1]):
                cnt -= 1
                if cnt < k:
                    return edges[i][2]
        return 0
