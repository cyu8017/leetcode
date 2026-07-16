# LeetCode 0372 - Super Pow
# https://leetcode.com/problems/super-pow/

from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        a %= mod

        def pow_mod(base: int, exponent: int) -> int:
            result = 1
            while exponent:
                if exponent & 1:
                    result = result * base % mod
                base = base * base % mod
                exponent >>= 1
            return result

        result = 1
        for digit in b:
            result = pow_mod(result, 10) * pow_mod(a, digit) % mod

        return result
