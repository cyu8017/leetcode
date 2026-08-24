# LeetCode 3561 - Resulting String After Adjacent Removals
# https://leetcode.com/problems/resulting-string-after-adjacent-removals/


def is_contiguous(a: str, b: str) -> bool:
    x = abs(ord(a) - ord(b))
    return x == 1 or x == 25


class Solution:
    def resultingString(self, s: str) -> str:
        stk = []
        for c in s:
            if stk and is_contiguous(stk[-1], c):
                stk.pop()
            else:
                stk.append(c)
        return "".join(stk)
