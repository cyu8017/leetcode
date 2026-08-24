# LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/


class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus = expression.index("+")
        left = expression[:plus]
        right = expression[plus + 1 :]
        best_val = float("inf")
        best = ""
        for i in range(len(left)):
            for j in range(1, len(right) + 1):
                a, b = left[:i], left[i:]
                c, d = right[:j], right[j:]
                val = int(b) + int(c)
                if a:
                    val *= int(a)
                if d:
                    val *= int(d)
                cand = f"{a}({b}+{c}){d}"
                if val < best_val:
                    best_val = val
                    best = cand
        return best
