# LeetCode 0409 - Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        odd = False
        for count in counts.values():
            length += count // 2 * 2
            if count % 2:
                odd = True
        return length + (1 if odd else 0)
