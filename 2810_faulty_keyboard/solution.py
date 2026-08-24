# LeetCode 2810 - Faulty Keyboard
# https://leetcode.com/problems/faulty-keyboard/


class Solution:
    def finalString(self, s: str) -> str:
        b = ""
        for c in s:
            if c == "i":
                b = b[::-1]
            else:
                b += c
        return b
