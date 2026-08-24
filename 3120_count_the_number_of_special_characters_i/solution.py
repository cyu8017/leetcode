# LeetCode 3120 - Count the Number of Special Characters I
# https://leetcode.com/problems/count-the-number-of-special-characters-i/


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = [False] * 128
        for ch in word:
            s[ord(ch)] = True
        ans = 0
        for i in range(26):
            if s[97 + i] and s[65 + i]:
                ans += 1
        return ans
