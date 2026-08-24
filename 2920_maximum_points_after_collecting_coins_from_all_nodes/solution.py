# LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
# https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

from typing import List


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        memo = {}

        def dfs(u: int, p: int, shifts: int) -> int:
            if shifts > 14:
                shifts = 14
            key = (u << 5) | shifts
            if key in memo:
                return memo[key]
            c = coins[u] >> shifts
            opt1 = c - k
            opt2 = c // 2
            for v in g[u]:
                if v == p:
                    continue
                opt1 += dfs(v, u, shifts)
                opt2 += dfs(v, u, shifts + 1)
            best = max(opt1, opt2)
            memo[key] = best
            return best

        return dfs(0, -1, 0)
