# LeetCode 3493 - Properties Graph
# https://leetcode.com/problems/properties-graph/

from typing import List


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        sets = [set(row) for row in properties]
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for i in range(n):
            for j in range(i + 1, n):
                cnt = 0
                for v in sets[i]:
                    if v in sets[j]:
                        cnt += 1
                if cnt >= k:
                    unite(i, j)
        comp = set()
        for i in range(n):
            comp.add(find(i))
        return len(comp)
