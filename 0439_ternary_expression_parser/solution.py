# LeetCode 0439 - Ternary Expression Parser
# https://leetcode.com/problems/ternary-expression-parser/


class Solution:
    def parseTernary(self, expression: str) -> str:
        if "?" not in expression:
            return expression

        separator = 2
        depth = 0
        for index in range(2, len(expression)):
            if expression[index] == "?":
                depth += 1
            elif expression[index] == ":":
                if depth == 0:
                    separator = index
                    break
                depth -= 1

        if expression[0] == "T":
            return self.parseTernary(expression[2:separator])
        return self.parseTernary(expression[separator + 1 :])
