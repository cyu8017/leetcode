# LeetCode 3174 - Clear Digits
# https://leetcode.com/problems/clear-digits/


class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        for c in s:
            if "0" <= c <= "9":
                stk.pop()
            else:
                stk.append(c)
        return "".join(stk)
