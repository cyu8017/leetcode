# LeetCode 2514 - Count Anagrams
# https://leetcode.com/problems/count-anagrams/

import re


class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 1000000007

        def mod_pow(a: int, e: int) -> int:
            res = 1
            a %= MOD
            while e > 0:
                if e & 1:
                    res = res * a % MOD
                a = a * a % MOD
                e >>= 1
            return res

        words = [] if s.strip() == "" else re.split(r"\s+", s.strip())
        max_n = 0
        for w in words:
            if len(w) > max_n:
                max_n = len(w)
        fact = [0] * (max_n + 1)
        inv_fact = [0] * (max_n + 1)
        fact[0] = 1
        for i in range(1, max_n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[max_n] = mod_pow(fact[max_n], MOD - 2)
        for i in range(max_n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        ans = 1
        for word in words:
            cnt = [0] * 26
            for ch in word:
                cnt[ord(ch) - 97] += 1
            cur = fact[len(word)]
            for c in cnt:
                cur = cur * inv_fact[c] % MOD
            ans = ans * cur % MOD
        return ans
