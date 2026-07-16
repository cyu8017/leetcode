# LeetCode 0405 - Convert a Number to Hexadecimal
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        digits = "0123456789abcdef"
        value = num & 0xFFFFFFFF
        result: list[str] = []

        while value:
            result.append(digits[value & 15])
            value >>= 4

        return "".join(reversed(result))
