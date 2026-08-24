# LeetCode 3536 - Maximum Product of Two Digits
# https://leetcode.com/problems/maximum-product-of-two-digits/


class Solution:
    def maxProduct(self, n: int) -> int:
        a, b = 0, 0
        while n > 0:
            x = n % 10
            n //= 10
            if a < x:
                b = a
                a = x
            elif b < x:
                b = x
        return a * b
