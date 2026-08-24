# LeetCode 2309 - Greatest English Letter in Upper and Lower Case
# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/


class Solution:
    def greatestLetter(self, s: str) -> str:
        lower = [False] * 26
        upper = [False] * 26
        for c in s:
            if "a" <= c <= "z":
                lower[ord(c) - 97] = True
            else:
                upper[ord(c) - 65] = True
        for i in range(25, -1, -1):
            if lower[i] and upper[i]:
                return chr(65 + i)
        return ""
