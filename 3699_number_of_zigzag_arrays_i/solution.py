# LeetCode 3699 - Number of ZigZag Arrays I
# https://leetcode.com/problems/number-of-zigzag-arrays-i/


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        if n == 1:
            return m % MOD
        up = [1] * m
        down = [1] * m
        for _ in range(2, n + 1):
            pref_down = [0] * (m + 1)
            for j in range(m):
                pref_down[j + 1] = (pref_down[j] + down[j]) % MOD
            nup = [pref_down[j] for j in range(m)]
            suf_up = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                suf_up[j] = (suf_up[j + 1] + up[j]) % MOD
            ndown = [suf_up[j + 1] for j in range(m)]
            up, down = nup, ndown
        ans = 0
        for j in range(m):
            ans = (ans + up[j]) % MOD
            ans = (ans + down[j]) % MOD
        return ans
