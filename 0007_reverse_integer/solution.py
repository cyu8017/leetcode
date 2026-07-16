# LeetCode 0007 - Reverse Integer
# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        limit = 2**31 - 1
        result = 0
        negative = x < 0
        x = abs(x)

        while x:
            result = result * 10 + x % 10
            x //= 10

        if result > limit:
            return 0
        return -result if negative else result
