# LeetCode 3612 - Process String with Special Operations I
# https://leetcode.com/problems/process-string-with-special-operations-i/


class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for c in s:
            if c.isalpha():
                result.append(c)
            elif c == "*":
                if result:
                    result.pop()
            elif c == "#":
                result = result + result
            elif c == "%":
                result.reverse()
        return "".join(result)
