# LeetCode 2872 - Maximum Number of K-Divisible Components
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/

from typing import List


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = 0

        def dfs(u: int, p: int) -> int:
            nonlocal ans
            s = values[u] % k
            for v in g[u]:
                if v == p:
                    continue
                s = (s + dfs(v, u)) % k
            if s == 0:
                ans += 1
            return s

        dfs(0, -1)
        return ans
