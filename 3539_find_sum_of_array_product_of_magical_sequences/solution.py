# LeetCode 3539 - Find Sum of Array Product of Magical Sequences
# https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

from typing import List


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        N, MOD = 31, 1000000007
        f = [0] * N
        g = [0] * N

        def qpow(a: int, kk: int) -> int:
            res = 1
            ba, bk = a, kk
            while bk > 0:
                if bk & 1:
                    res = res * ba % MOD
                ba = ba * ba % MOD
                bk >>= 1
            return res

        f[0] = g[0] = 1
        for i in range(1, N):
            f[i] = f[i - 1] * i % MOD
            g[i] = qpow(f[i], MOD - 2)

        def comb(mm: int, nn: int) -> int:
            if nn < 0 or nn > mm:
                return 0
            return f[mm] * g[nn] % MOD * g[mm - nn] % MOD

        n = len(nums)
        dp = [[[[-1] * N for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

        def dfs(i: int, j: int, kk: int, st: int) -> int:
            if kk < 0 or (i == n and j > 0):
                return 0
            if i == n:
                while st > 0:
                    kk -= st & 1
                    st >>= 1
                return 1 if kk == 0 else 0
            if dp[i][j][kk][st] != -1:
                return dp[i][j][kk][st]
            res = 0
            for t in range(j + 1):
                nt = t + st
                nk = kk - (nt & 1)
                p = qpow(nums[i], t)
                tmp = comb(j, t) * p % MOD * dfs(i + 1, j - t, nk, nt >> 1) % MOD
                res = (res + tmp) % MOD
            dp[i][j][kk][st] = res
            return res

        return dfs(0, m, k, 0)
