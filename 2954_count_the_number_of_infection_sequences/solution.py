# LeetCode 2954 - Count the Number of Infection Sequences
# https://leetcode.com/problems/count-the-number-of-infection-sequences/

from typing import List

MOD = 1000000007


def modPow(a: int, b: int) -> int:
    res = 1
    a %= MOD
    while b > 0:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res


class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        fact = [0] * (n + 1)
        inv_fact = [0] * (n + 1)
        fact[0] = 1
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[n] = modPow(fact[n], MOD - 2)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        m = len(sick)
        total_empty = n - m
        ans = fact[total_empty]
        prev = -1
        for s in sick:
            gap = s - prev - 1
            if prev == -1:
                ans = ans * inv_fact[gap] % MOD
            elif gap > 0:
                ans = ans * inv_fact[gap] % MOD * modPow(2, gap - 1) % MOD
            prev = s
        gap2 = n - prev - 1
        ans = ans * inv_fact[gap2] % MOD
        return ans
