# LeetCode 0625 - Minimum Factorization
# https://leetcode.com/problems/minimum-factorization/


class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 10:
            return num

        digits: list[int] = []
        for digit in range(9, 1, -1):
            while num % digit == 0:
                digits.append(digit)
                num //= digit

        if num != 1:
            return 0

        result = 0
        for digit in reversed(digits):
            result = result * 10 + digit
            if result > 2**31 - 1:
                return 0
        return result
