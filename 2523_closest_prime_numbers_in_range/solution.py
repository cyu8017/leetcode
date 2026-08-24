# LeetCode 2523 - Closest Prime Numbers in Range
# https://leetcode.com/problems/closest-prime-numbers-in-range/

from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right + 1)
        if right >= 0:
            is_prime[0] = False
        if right >= 1:
            is_prime[1] = False
        i = 2
        while i * i <= right:
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False
            i += 1
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        if len(primes) < 2:
            return [-1, -1]
        best_diff = 10**18
        best = [-1, -1]
        for i in range(len(primes) - 1):
            d = primes[i + 1] - primes[i]
            if d < best_diff:
                best_diff = d
                best = [primes[i], primes[i + 1]]
        return best
