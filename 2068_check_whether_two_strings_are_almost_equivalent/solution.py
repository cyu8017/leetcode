# LeetCode 2068 - Check Whether Two Strings are Almost Equivalent
# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq = [0] * 26
        for i in range(len(word1)):
            freq[ord(word1[i]) - 97] += 1
            freq[ord(word2[i]) - 97] -= 1
        return all(-3 <= v <= 3 for v in freq)
