# LeetCode 3614 - Process String with Special Operations II
# https://leetcode.com/problems/process-string-with-special-operations-ii/


class Solution:
    def processStr(self, s: str, k: int) -> str:
        m = 0
        for c in s:
            if c == "*":
                m = m - 1 if m > 0 else 0
            elif c == "#":
                m <<= 1
            elif c != "%":
                m += 1
        k2 = k
        if k2 >= m:
            return "."
        i = len(s) - 1
        while True:
            c = s[i]
            if c == "*":
                m += 1
            elif c == "#":
                m //= 2
                if k2 >= m:
                    k2 -= m
            elif c == "%":
                k2 = m - 1 - k2
            else:
                m -= 1
                if k2 == m:
                    return c
            i -= 1
