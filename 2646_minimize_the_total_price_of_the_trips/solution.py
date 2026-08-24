# LeetCode 2646 - Minimize the Total Price of the Trips
# https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

from typing import List


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        cnt = [0] * n

        def path(u: int, p: int, target: int) -> bool:
            if u == target:
                cnt[u] += 1
                return True
            for v in g[u]:
                if v == p:
                    continue
                if path(v, u, target):
                    cnt[u] += 1
                    return True
            return False

        for a, b in trips:
            path(a, -1, b)

        def dfs(u: int, p: int):
            full = price[u] * cnt[u]
            half = full // 2
            for v in g[u]:
                if v == p:
                    continue
                child = dfs(v, u)
                full += min(child[0], child[1])
                half += child[0]
            return (full, half)

        res = dfs(0, -1)
        return min(res[0], res[1])
