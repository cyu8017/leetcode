# LeetCode 0357 - Count Numbers with Unique Digits
# https://leetcode.com/problems/count-numbers-with-unique-digits/


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        total = 10
        unique = 9
        available = 9

        for length in range(2, n + 1):
            unique *= available
            available -= 1
            total += unique

        return total
