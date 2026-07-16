# LeetCode 0772 - Basic Calculator III
# https://leetcode.com/problems/basic-calculator-iii/


class Solution:
    def calculate(self, s: str) -> int:
        def parse(expr: str, i: int) -> tuple[int, int]:
            stack: list[int] = []
            num = 0
            sign = "+"
            while i < len(expr):
                ch = expr[i]
                if ch.isdigit():
                    num = num * 10 + int(ch)
                if ch == "(":
                    num, i = parse(expr, i + 1)
                if ch in "+-*/)" or i == len(expr) - 1:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        stack.append(stack.pop() * num)
                    else:
                        top = stack.pop()
                        stack.append(int(top / num))
                    if ch == ")":
                        return sum(stack), i
                    sign = ch
                    num = 0
                i += 1
            return sum(stack), i

        return parse(s.replace(" ", ""), 0)[0]
