# LeetCode 1096 - Brace Expansion II
# https://leetcode.com/problems/brace-expansion-ii/

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(expr: str, i: int) -> tuple[set[str], int]:
            union: set[str] = set()
            cur: set[str] = {""}
            while i < len(expr) and expr[i] != "}":
                if expr[i] == "{":
                    nested, i = parse(expr, i + 1)
                    cur = {a + b for a in cur for b in nested}
                elif expr[i] == ",":
                    union |= cur
                    cur = {""}
                    i += 1
                else:
                    j = i
                    while j < len(expr) and expr[j].isalpha():
                        j += 1
                    token = expr[i:j]
                    cur = {a + token for a in cur}
                    i = j
            union |= cur
            return union, i + 1

        result, _ = parse(expression, 0)
        return sorted(result)
