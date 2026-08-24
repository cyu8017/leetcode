# LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

from typing import List


class UnionFind3600:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.size = [1] * n
        self.cnt = n

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
        self.cnt -= 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def check(lim: int) -> bool:
            uf = UnionFind3600(n)
            for e in edges:
                if e[2] >= lim:
                    uf.unite(e[0], e[1])
            rem = k
            for e in edges:
                if e[2] * 2 >= lim and rem > 0:
                    if uf.unite(e[0], e[1]):
                        rem -= 1
            return uf.cnt == 1

        uf = UnionFind3600(n)
        mn = 1000000
        for e in edges:
            if e[3] == 1:
                mn = min(mn, e[2])
                if not uf.unite(e[0], e[1]):
                    return -1
        for e in edges:
            uf.unite(e[0], e[1])
        if uf.cnt > 1:
            return -1
        l, r = 1, mn
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
