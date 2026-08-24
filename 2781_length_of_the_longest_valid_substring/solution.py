# LeetCode 2781 - Length of the Longest Valid Substring
# https://leetcode.com/problems/length-of-the-longest-valid-substring/

from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbid = set(forbidden)
        max_len = 0
        for f in forbidden:
            max_len = max(max_len, len(f))
        ans = 0
        right = len(word) - 1
        for left in range(len(word) - 1, -1, -1):
            for k in range(left, right + 1):
                if k - left + 1 > max_len:
                    break
                if word[left : k + 1] in forbid:
                    right = k - 1
                    break
            ans = max(ans, right - left + 1)
        return ans
