from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.components = n
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.parent[a] = b
        self.components -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob, used = DSU(n), DSU(n), 0
        for t, u, v in edges:
            if t == 3:
                merged = alice.union(u, v)
                bob.union(u, v)
                used += merged
        for t, u, v in edges:
            if t == 1:
                used += alice.union(u, v)
            elif t == 2:
                used += bob.union(u, v)
        return len(edges) - used if alice.components == bob.components == 1 else -1
