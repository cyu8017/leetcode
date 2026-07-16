# LeetCode 0241 - Different Ways to Add Parentheses
# https://leetcode.com/problems/different-ways-to-add-parentheses/

from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        result: list[int] = []
        for index, char in enumerate(expression):
            if char not in "+-*":
                continue
            left = self.diffWaysToCompute(expression[:index])
            right = self.diffWaysToCompute(expression[index + 1 :])
            for left_value in left:
                for right_value in right:
                    if char == "+":
                        result.append(left_value + right_value)
                    elif char == "-":
                        result.append(left_value - right_value)
                    else:
                        result.append(left_value * right_value)
        return result
