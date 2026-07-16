# LeetCode 0227 - Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/


class Solution:
    def calculate(self, s: str) -> int:
        stack: list[int] = []
        number = 0
        operator = "+"
        for index, char in enumerate(s):
            if char.isdigit():
                number = number * 10 + int(char)
            if char in "+-*/" or index == len(s) - 1:
                if operator == "+":
                    stack.append(number)
                elif operator == "-":
                    stack.append(-number)
                elif operator == "*":
                    stack.append(stack.pop() * number)
                elif operator == "/":
                    stack.append(int(stack.pop() / number))
                operator = char
                number = 0
        return sum(stack)
