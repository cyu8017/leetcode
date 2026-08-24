# LeetCode 2403 - Minimum Time to Kill All Monsters
# https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

from typing import List


class Solution:
    def minimumTime(self, power: List[int]) -> int:
        def bit_count(x: int) -> int:
            c = 0
            while x != 0:
                c += x & 1
                x >>= 1
            return c

        n = len(power)
        N = 1 << n
        dp = [10**18] * N
        dp[0] = 0
        for mask in range(N):
            killed = bit_count(mask)
            gain = killed + 1
            for i in range(n):
                if (mask & (1 << i)) != 0:
                    continue
                need = (power[i] + gain - 1) // gain
                nm = mask | (1 << i)
                dp[nm] = min(dp[nm], dp[mask] + need)
        return dp[N - 1]
