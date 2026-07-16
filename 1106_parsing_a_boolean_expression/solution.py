# LeetCode 1106 - Parsing A Boolean Expression
# https://leetcode.com/problems/parsing-a-boolean-expression/

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack: list[str] = []
        for ch in expression:
            if ch == ")":
                values: list[bool] = []
                while stack and stack[-1] not in "&|!":
                    token = stack.pop()
                    if token in "tf":
                        values.append(token == "t")
                op = stack.pop()
                if op == "!":
                    stack.append("t" if not values[0] else "f")
                elif op == "&":
                    stack.append("t" if all(values) else "f")
                else:
                    stack.append("t" if any(values) else "f")
            elif ch != ",":
                stack.append(ch)
        return stack[-1] == "t"
