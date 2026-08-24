# LeetCode 3099 - Harshad Number
# https://leetcode.com/problems/harshad-number/


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        y = x
        while y > 0:
            s += y % 10
            y //= 10
        return s if x % s == 0 else -1
