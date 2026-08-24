# LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
# https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

from typing import List, Optional

MX3896 = 200000
isPrime3896: Optional[List[bool]] = None
primes3896: Optional[List[int]] = None


def init3896() -> None:
    global isPrime3896, primes3896
    if isPrime3896 is not None:
        return
    isPrime3896 = [True] * (MX3896 + 1)
    isPrime3896[0] = isPrime3896[1] = False
    i = 2
    while i * i <= MX3896:
        if isPrime3896[i]:
            j = i * i
            while j <= MX3896:
                isPrime3896[j] = False
                j += i
        i += 1
    primes3896 = []
    for i in range(2, MX3896 + 1):
        if isPrime3896[i]:
            primes3896.append(i)


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        init3896()
        ans = 0
        for i in range(len(nums)):
            x = nums[i]
            if i % 2 == 0:
                lo = 0
                hi = len(primes3896)
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if primes3896[mid] < x:
                        lo = mid + 1
                    else:
                        hi = mid
                ans += primes3896[lo] - x
            elif isPrime3896[x]:
                ans += 2 if x == 2 else 1
        return ans
