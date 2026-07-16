from bisect import bisect_left
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]


class DistanceLimitedPathsExist:
    def __init__(self, n: int, edgeList: List[List[int]]):
        self.edges = sorted((w, u, v) for u, v, w in edgeList)
        self.weights = []
        self.versions = []
        dsu = DSU(n)
        i = 0
        while i < len(self.edges):
            weight = self.edges[i][0]
            while i < len(self.edges) and self.edges[i][0] == weight:
                _, u, v = self.edges[i]
                dsu.union(u, v)
                i += 1
            self.weights.append(weight)
            self.versions.append(tuple(dsu.parent))

    def query(self, p: int, q: int, limit: int) -> bool:
        idx = bisect_left(self.weights, limit) - 1
        if idx < 0:
            return p == q
        parent = self.versions[idx]

        def find(x: int) -> int:
            while parent[x] != x:
                x = parent[x]
            return x

        return find(p) == find(q)
