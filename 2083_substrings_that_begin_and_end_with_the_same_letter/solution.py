# LeetCode 2083 - Substrings That Begin and End With the Same Letter
# https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = [0] * 26
        ans = 0
        for c in s:
            i = ord(c) - 97
            freq[i] += 1
            ans += freq[i]
        return ans
