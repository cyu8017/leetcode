# LeetCode 0395 - Longest Substring with At Least K Repeating Characters
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0

        counts = Counter(s)
        for char, count in counts.items():
            if count < k:
                return max(self.longestSubstring(part, k) for part in s.split(char))
        return len(s)
