# LeetCode 2847 - Smallest Number With Given Digit Product
# https://leetcode.com/problems/smallest-number-with-given-digit-product/


class Solution:
    def smallestNumber(self, n: int) -> str:
        if n == 0:
            return "0"
        if n == 1:
            return "1"
        digits = []
        for d in range(9, 1, -1):
            while n % d == 0:
                digits.append(str(d))
                n //= d
        if n > 1:
            return "-1"
        return "".join(reversed(digits))
