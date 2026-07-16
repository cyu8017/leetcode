# LeetCode 0479 - Largest Palindrome Product
# https://leetcode.com/problems/largest-palindrome-product/


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10**n - 1
        lower = 10 ** (n - 1)
        for first in range(upper, lower - 1, -1):
            candidate = int(str(first) + str(first)[::-1])
            factor = upper
            while factor * factor >= candidate:
                if candidate % factor == 0 and lower <= candidate // factor <= upper:
                    return candidate % 1337
                factor -= 1
        return 0
