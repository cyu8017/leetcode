# LeetCode 3756 - Concatenate Non Zero Digits and Multiply by Sum II
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MX = 100001
        MOD = 1000000007
        PW = [0] * MX
        PW[0] = 1
        for i in range(1, MX):
            PW[i] = PW[i - 1] * 10 % MOD
        n = len(s)
        sumD = [0] * (n + 1)
        cntN0 = [0] * (n + 1)
        p = [0] * (n + 1)
        for i in range(1, n + 1):
            d = ord(s[i - 1]) - 48
            sumD[i] = sumD[i - 1] + d
            cntN0[i] = cntN0[i - 1]
            if d > 0:
                cntN0[i] += 1
                p[i] = (p[i - 1] * 10 + d) % MOD
            else:
                p[i] = p[i - 1]
        ans = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            n0 = cntN0[r + 1] - cntN0[l]
            sd = sumD[r + 1] - sumD[l]
            x = (p[r + 1] - p[l] * PW[n0] % MOD + MOD) % MOD
            ans[i] = x * sd % MOD
        return ans
