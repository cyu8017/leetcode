# LeetCode 3589 - Count Prime-Gap Balanced Subarrays
# https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

from typing import List


class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        is_prime = [False] * (mx + 1)
        for i in range(2, mx + 1):
            is_prime[i] = True
        i = 2
        while i * i <= mx:
            if is_prime[i]:
                for j in range(i * i, mx + 1, i):
                    is_prime[j] = False
            i += 1
        n = len(nums)
        ans = 0
        for l in range(n):
            primes = []
            for r in range(l, n):
                if is_prime[nums[r]]:
                    primes.append(nums[r])
                if len(primes) >= 2:
                    mn = mxp = primes[0]
                    for p in primes:
                        mn = min(mn, p)
                        mxp = max(mxp, p)
                    if mxp - mn <= k:
                        ans += 1
        return ans
