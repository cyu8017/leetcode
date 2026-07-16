# LeetCode 0640 - Solve the Equation
# https://leetcode.com/problems/solve-the-equation/

import re


class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr: str) -> tuple[int, int]:
            coef = const = 0
            for token in re.findall(r"[+-]?(?:\d+x|x|\d+)", expr):
                if "x" in token:
                    raw = token.replace("x", "")
                    if raw in ("", "+"):
                        coef += 1
                    elif raw == "-":
                        coef -= 1
                    else:
                        coef += int(raw)
                else:
                    const += int(token)
            return coef, const

        left, right = equation.split("=")
        left_coef, left_const = parse(left)
        right_coef, right_const = parse(right)
        coef = left_coef - right_coef
        const = right_const - left_const

        if coef == 0:
            return "Infinite solutions" if const == 0 else "No solution"
        return f"x={const // coef}"
