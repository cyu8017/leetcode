# LeetCode 3749 - Evaluate Valid Expressions
# https://leetcode.com/problems/evaluate-valid-expressions/

from typing import List, Tuple


class Solution:
    def evaluateExpression(self, expression: str) -> int:
        def parse(i: int) -> Tuple[int, int]:
            ch = expression[i]
            if ("0" <= ch <= "9") or ch == "-":
                j = i
                if expression[j] == "-":
                    j += 1
                while j < len(expression) and "0" <= expression[j] <= "9":
                    j += 1
                return int(expression[i:j]), j
            j = i
            while expression[j] != "(":
                j += 1
            op = expression[i:j]
            j += 1
            p1 = parse(j)
            j = p1[1] + 1
            p2 = parse(j)
            j = p2[1] + 1
            res = 0
            if op == "add":
                res = p1[0] + p2[0]
            elif op == "sub":
                res = p1[0] - p2[0]
            elif op == "mul":
                res = p1[0] * p2[0]
            elif op == "div":
                res = int(p1[0] / p2[0])
            return res, j

        return parse(0)[0]
