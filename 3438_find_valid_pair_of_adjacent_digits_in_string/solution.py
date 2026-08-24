# LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
# https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/


class Solution:
    def findValidPair(self, s: str) -> str:
        freq = [0] * 10
        for c in s:
            freq[ord(c) - 48] += 1
        for i in range(len(s) - 1):
            a = ord(s[i]) - 48
            b = ord(s[i + 1]) - 48
            if a != b and freq[a] == a and freq[b] == b:
                return s[i : i + 2]
        return ""
