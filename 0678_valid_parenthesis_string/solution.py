# LeetCode 0678 - Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/


class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for ch in s:
            if ch == "(":
                lo += 1
                hi += 1
            elif ch == ")":
                lo = max(lo - 1, 0)
                hi -= 1
                if hi < 0:
                    return False
            else:
                lo = max(lo - 1, 0)
                hi += 1
        return lo == 0
