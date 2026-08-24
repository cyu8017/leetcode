# LeetCode 3700 - Number of ZigZag Arrays II
# https://leetcode.com/problems/number-of-zigzag-arrays-ii/


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        if n == 1:
            return m % MOD
        up = [1] * m
        down = [1] * m
        for _ in range(2, n + 1):
            pref = [0] * (m + 1)
            for j in range(m):
                pref[j + 1] = (pref[j] + down[j]) % MOD
            nup = [pref[j] for j in range(m)]
            suf = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                suf[j] = (suf[j + 1] + up[j]) % MOD
            ndown = [suf[j + 1] for j in range(m)]
            up, down = nup, ndown
        ans = 0
        for j in range(m):
            ans = (ans + up[j]) % MOD
            ans = (ans + down[j]) % MOD
        return ans
