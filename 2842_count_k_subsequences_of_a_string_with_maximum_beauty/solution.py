# LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
# https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 1000000007
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        vals = sorted((f for f in freq if f > 0), reverse=True)
        if len(vals) < k:
            return 0
        threshold = vals[k - 1]
        need = 0
        avail = 0
        prod = 1
        for v in vals:
            if v > threshold:
                prod = (prod * v) % MOD
                need += 1
            elif v == threshold:
                avail += 1
        remain = k - need

        def mod_pow(a: int, b: int) -> int:
            res = 1
            a %= MOD
            while b > 0:
                if b & 1:
                    res = (res * a) % MOD
                a = (a * a) % MOD
                b >>= 1
            return res

        def comb(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            num = 1
            den = 1
            for i in range(r):
                num = (num * (n - i)) % MOD
                den = (den * (i + 1)) % MOD
            return (num * mod_pow(den, MOD - 2)) % MOD

        prod = (prod * comb(avail, remain)) % MOD
        for _ in range(remain):
            prod = (prod * threshold) % MOD
        return prod
