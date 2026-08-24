# LeetCode 3121 - Count the Number of Special Characters II
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first = [0] * 128
        last = [0] * 128
        for i, ch in enumerate(word):
            c = ord(ch)
            if first[c] == 0:
                first[c] = i + 1
            last[c] = i + 1
        ans = 0
        for i in range(26):
            if last[97 + i] > 0 and last[97 + i] < first[65 + i]:
                ans += 1
        return ans
