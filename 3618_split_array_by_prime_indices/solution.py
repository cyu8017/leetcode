# LeetCode 3618 - Split Array by Prime Indices
# https://leetcode.com/problems/split-array-by-prime-indices/

from typing import List, Optional

_PRIMES3618: Optional[List[bool]] = None


def primes3618() -> List[bool]:
    global _PRIMES3618
    if _PRIMES3618 is None:
        m = 100010
        primes = [True] * m
        primes[0] = primes[1] = False
        for i in range(2, m):
            if primes[i]:
                for j in range(i + i, m, i):
                    primes[j] = False
        _PRIMES3618 = primes
    return _PRIMES3618


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        pr = primes3618()
        ans = 0
        for i, x in enumerate(nums):
            if pr[i]:
                ans += x
            else:
                ans -= x
        return abs(ans)
