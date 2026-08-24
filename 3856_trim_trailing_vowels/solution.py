# LeetCode 3856 - Trim Trailing Vowels
# https://leetcode.com/problems/trim-trailing-vowels/


class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        def is_vowel(c: str) -> bool:
            return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"

        i = len(s) - 1
        while i >= 0 and is_vowel(s[i]):
            i -= 1
        return s[: i + 1]
