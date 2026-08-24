# LeetCode 3233 - Find the Count of Numbers Which Are Not Special
# https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

import math


class Solution:
    _primes = None

    def nonSpecialCount(self, l: int, r: int) -> int:
        M = 31623
        if Solution._primes is None:
            primes = [True] * (M + 1)
            primes[0] = primes[1] = False
            for i in range(2, M + 1):
                if primes[i]:
                    for j in range(i * 2, M + 1, i):
                        primes[j] = False
            Solution._primes = primes
        primes = Solution._primes
        lo = math.ceil(math.sqrt(l))
        hi = math.floor(math.sqrt(r))
        cnt = 0
        for i in range(lo, hi + 1):
            if primes[i]:
                cnt += 1
        return r - l + 1 - cnt
