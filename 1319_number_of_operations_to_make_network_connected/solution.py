# LeetCode 1319 - Number Of Operations To Make Network Connected

from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        parent = list(range(n))
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        for a, b in connections:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
        return len({find(i) for i in range(n)}) - 1
