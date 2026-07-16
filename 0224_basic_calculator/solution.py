# LeetCode 0224 - Basic Calculator
# https://leetcode.com/problems/basic-calculator/


class Solution:
    def calculate(self, s: str) -> int:
        stack: list[int] = []
        result = 0
        number = 0
        sign = 1
        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char in "+-":
                result += sign * number
                number = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
        result += sign * number
        return result
