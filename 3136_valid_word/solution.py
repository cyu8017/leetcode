# LeetCode 3136 - Valid Word
# https://leetcode.com/problems/valid-word/


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        has_vowel = False
        has_consonant = False
        vs = [False] * 26
        for c in "aeiou":
            vs[ord(c) - 97] = True
        for c in word:
            if c.isalpha():
                lower = c.lower()
                if vs[ord(lower) - 97]:
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isdigit():
                return False
        return has_vowel and has_consonant
