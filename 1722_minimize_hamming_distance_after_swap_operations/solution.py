from collections import Counter, defaultdict
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        dsu = DSU(len(source))
        for a, b in allowedSwaps:
            dsu.union(a, b)
        groups = defaultdict(Counter)
        for i, value in enumerate(source):
            groups[dsu.find(i)][value] += 1
        ans = 0
        for i, value in enumerate(target):
            group = groups[dsu.find(i)]
            if group[value]:
                group[value] -= 1
            else:
                ans += 1
        return ans
