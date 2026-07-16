# LeetCode 0917 - Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        i, j = 0, len(chars) - 1
        while i < j:
            while i < j and not chars[i].isalpha():
                i += 1
            while i < j and not chars[j].isalpha():
                j -= 1
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        return "".join(chars)
