# LeetCode 2539 - Count the Number of Good Subsequences
# https://leetcode.com/problems/count-the-number-of-good-subsequences/


class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        MOD = 1000000007
        cnt = [0] * 26
        maxf = 0
        for c in s:
            idx = ord(c) - 97
            cnt[idx] += 1
            if cnt[idx] > maxf:
                maxf = cnt[idx]

        def mod_pow(a: int, e: int) -> int:
            res = 1
            while e > 0:
                if e & 1:
                    res = res * a % MOD
                a = a * a % MOD
                e >>= 1
            return res

        fact = [0] * (maxf + 1)
        inv_fact = [0] * (maxf + 1)
        fact[0] = 1
        for i in range(1, maxf + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[maxf] = mod_pow(fact[maxf], MOD - 2)
        for i in range(maxf, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(n: int, k: int) -> int:
            if k < 0 or k > n:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

        ans = 0
        for k in range(1, maxf + 1):
            ways = 1
            for i in range(26):
                if cnt[i] >= k:
                    ways = ways * (1 + comb(cnt[i], k)) % MOD
            ans = (ans + ways - 1 + MOD) % MOD
        return ans
