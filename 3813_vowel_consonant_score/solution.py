# LeetCode 3813 - Vowel Consonant Score
# https://leetcode.com/problems/vowel-consonant-score/

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = 0
        c = 0
        for ch in s:
            if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
                c += 1
                if ch in "aeiou":
                    v += 1
        c -= v
        if c == 0:
            return 0
        return v // c
