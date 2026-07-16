# LeetCode 0400 - Nth Digit
# https://leetcode.com/problems/nth-digit/


class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        count = 9
        start = 1

        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10

        number = start + (n - 1) // digits
        return int(str(number)[(n - 1) % digits])
