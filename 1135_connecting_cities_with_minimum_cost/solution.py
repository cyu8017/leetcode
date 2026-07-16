# LeetCode 1135 - Connecting Cities With Minimum Cost
# https://leetcode.com/problems/connecting-cities-with-minimum-cost/

class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        parent = list(range(n + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[rb] = ra
            return True

        connections.sort(key=lambda x: x[2])
        cost = edges = 0
        for a, b, w in connections:
            if union(a, b):
                cost += w
                edges += 1
                if edges == n - 1:
                    return cost
        return -1
