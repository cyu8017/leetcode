# LeetCode 0050 - Pow(x, n)
# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < 0:
            x = 1.0 / x
            n = -n

        result = 1.0
        current = x

        while n:
            if n & 1:
                result *= current
            current *= current
            n >>= 1

        return result
