# LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/


class Solution:
    def smallestValue(self, n: int) -> int:
        def sum_prime_factors(x: int) -> int:
            s = 0
            i = 2
            while i * i <= x:
                while x % i == 0:
                    s += i
                    x //= i
                i += 1
            if x > 1:
                s += x
            return s

        while True:
            s = sum_prime_factors(n)
            if s == n:
                return n
            n = s
