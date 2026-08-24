# LeetCode 3345 - Smallest Divisible Digit Product I
# https://leetcode.com/problems/smallest-divisible-digit-product-i/


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        x = n
        while True:
            p = 1
            y = x
            while y > 0:
                p *= y % 10
                y //= 10
            if p % t == 0:
                return x
            x += 1
