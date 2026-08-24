# LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        i = 0
        while i < len(str1) and j < len(str2):
            a = ord(str1[i]) - 97
            b = ord(str2[j]) - 97
            if a == b or (a + 1) % 26 == b:
                j += 1
            i += 1
        return j == len(str2)
