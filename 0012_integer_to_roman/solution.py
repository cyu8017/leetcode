# LeetCode 0012 - Integer to Roman
# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = []

        for value, symbol in zip(values, symbols):
            while num >= value:
                result.append(symbol)
                num -= value

        return "".join(result)
