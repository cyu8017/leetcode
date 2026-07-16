# LeetCode 1168 - Optimize Water Distribution in a Village
# https://leetcode.com/problems/optimize-water-distribution-in-a-village/

class Solution:
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
        parent = list(range(n + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        edges = [[0, i + 1, w] for i, w in enumerate(wells)] + pipes
        edges.sort(key=lambda e: e[2])
        ans = 0
        for a, b, cost in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                continue
            parent[rb] = ra
            ans += cost
        return ans
