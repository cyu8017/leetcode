# LeetCode 0848 - Shifting Letters
# https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total = 0
        chars = list(s)
        for i in range(len(s) - 1, -1, -1):
            total = (total + shifts[i]) % 26
            chars[i] = chr((ord(chars[i]) - 97 + total) % 26 + 97)
        return "".join(chars)
