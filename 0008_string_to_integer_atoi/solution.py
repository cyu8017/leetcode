# LeetCode 0008 - String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:
        int_max = 2**31 - 1
        int_min = -2**31
        i = 0
        n = len(s)

        while i < n and s[i] == " ":
            i += 1
        if i >= n:
            return 0

        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")
            if result > (int_max - digit) // 10:
                return int_min if sign == -1 else int_max
            result = result * 10 + digit
            i += 1

        return sign * result
