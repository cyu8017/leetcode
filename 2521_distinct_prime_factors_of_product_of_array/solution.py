# LeetCode 2521 - Distinct Prime Factors of Product of Array
# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            x = num
            p = 2
            while p * p <= x:
                if x % p == 0:
                    seen.add(p)
                    while x % p == 0:
                        x //= p
                p += 1
            if x > 1:
                seen.add(x)
        return len(seen)
