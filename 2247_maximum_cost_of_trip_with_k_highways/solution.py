# LeetCode 2247 - Maximum Cost of Trip With K Highways
# https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

from typing import List


class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        if k + 1 > n:
            return -1
        g = [[] for _ in range(n)]
        for a, b, w in highways:
            g[a].append((b, w))
            g[b].append((a, w))
        dp = [[-1] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 0
        ans = -1
        for mask in range(1 << n):
            cities = bin(mask).count("1")
            for u in range(n):
                if dp[mask][u] < 0:
                    continue
                if cities - 1 == k:
                    ans = max(ans, dp[mask][u])
                for v, w in g[u]:
                    if mask & (1 << v):
                        continue
                    nm = mask | (1 << v)
                    dp[nm][v] = max(dp[nm][v], dp[mask][u] + w)
        return ans
