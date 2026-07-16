# LeetCode 0467 - Unique Substrings in Wraparound String
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        counts = [0] * 26
        length = 0
        for index, char in enumerate(s):
            if index > 0 and (ord(char) - ord(s[index - 1]) + 26) % 26 == 1:
                length += 1
            else:
                length = 1
            position = ord(char) - ord("a")
            counts[position] = max(counts[position], length)
        return sum(counts)
