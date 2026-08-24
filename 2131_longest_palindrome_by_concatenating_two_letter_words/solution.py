# LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from typing import List
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = {}
        for w in words:
            freq[w] = (freq.get(w) or 0) + 1
        ans = 0
        center = False
        for w, c in freq.items():
            rev = w[1] + w[0]
            if w[0] == w[1]:
                ans += c // 2 * 4
                if c % 2 != 0:
                    center = True
            elif w < rev:
                ans += min(c, freq.get(rev) or 0) * 4
        if center:
            ans += 2
        return ans
