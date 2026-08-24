# LeetCode 3754 - Concatenate Non Zero Digits and Multiply by Sum I
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        p, x, s = 1, 0, 0
        while n > 0:
            v = n % 10
            if v != 0:
                s += v
                x += p * v
                p *= 10
            n //= 10
        return x * s
