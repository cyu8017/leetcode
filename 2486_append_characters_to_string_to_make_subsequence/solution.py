# LeetCode 2486 - Append Characters to String to Make Subsequence
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        i = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return len(t) - j
