# LeetCode 0150 - Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(int(token))
        return stack[-1]
