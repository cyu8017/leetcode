# LeetCode 3444 - Minimum Increments for Target Multiples in an Array
# https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

from typing import List


class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def lcm(a: int, b: int) -> int:
            return a // gcd(a, b) * b

        m = len(target)
        N = 1 << m
        inf = 10**18
        dp = [inf] * N
        dp[0] = 0
        for x in nums:
            ndp = dp[:]
            for mask in range(N):
                for sub in range(1, N):
                    L = 1
                    ok = True
                    for i in range(m):
                        if sub & (1 << i):
                            L = lcm(L, target[i])
                            if L > 1000000000:
                                ok = False
                                break
                    if not ok:
                        continue
                    cost = (L - x % L) % L
                    nmask = mask | sub
                    if dp[mask] + cost < ndp[nmask]:
                        ndp[nmask] = dp[mask] + cost
            dp = ndp
        return dp[N - 1]
