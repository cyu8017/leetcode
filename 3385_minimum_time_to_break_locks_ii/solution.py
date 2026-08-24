# LeetCode 3385 - Minimum Time to Break Locks II
# https://leetcode.com/problems/minimum-time-to-break-locks-ii/

from typing import List


def bitsOnes(x: int) -> int:
    c = 0
    while x > 0:
        c += x & 1
        x >>= 1
    return c


class Solution:
    def findMinimumTime(self, strength: List[int]) -> int:
        n = len(strength)
        N = 1 << n
        inf = 1e18
        dp = [inf] * N
        dp[0] = 0
        k = 1
        for mask in range(N):
            if dp[mask] == inf:
                continue
            opened = bitsOnes(mask)
            x = 1 + opened * k
            for i in range(n):
                if (mask & (1 << i)) != 0:
                    continue
                t = (strength[i] + x - 1) // x
                nmask = mask | (1 << i)
                if dp[mask] + t < dp[nmask]:
                    dp[nmask] = dp[mask] + t
        return int(dp[N - 1])
