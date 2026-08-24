# LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
# https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

from typing import List


class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        def popcount(x: int) -> int:
            c = 0
            while x != 0:
                c += x & 1
                x >>= 1
            return c

        need = [0] * n
        dp = [-1] * (1 << n)
        dp[0] = 0
        for e in edges:
            need[e[1]] |= 1 << e[0]
        for mask in range(1 << n):
            if dp[mask] < 0:
                continue
            pos = popcount(mask) + 1
            for i in range(n):
                if ((mask >> i) & 1) != 0:
                    continue
                if (mask & need[i]) == need[i]:
                    nm = mask | (1 << i)
                    v = dp[mask] + score[i] * pos
                    if v > dp[nm]:
                        dp[nm] = v
        return dp[(1 << n) - 1]
