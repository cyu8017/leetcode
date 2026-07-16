# LeetCode 0005 - Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start = 0
        best_len = 0

        def expand(left: int, right: int) -> None:
            nonlocal best_start, best_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1
            if length > best_len:
                best_len = length
                best_start = left + 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[best_start : best_start + best_len]
