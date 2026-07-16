# LeetCode 1175 - Prime Arrangements
# https://leetcode.com/problems/prime-arrangements/

import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            for d in range(2, int(x**0.5) + 1):
                if x % d == 0:
                    return False
            return True

        primes = sum(1 for i in range(1, n + 1) if is_prime(i))
        return (math.factorial(primes) * math.factorial(n - primes)) % MOD
