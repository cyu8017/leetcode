# LeetCode 0504 - Base 7
# https://leetcode.com/problems/base-7/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        digits: list[str] = []
        while num:
            digits.append(str(num % 7))
            num //= 7
        result = "".join(reversed(digits))
        return f"-{result}" if negative else result
