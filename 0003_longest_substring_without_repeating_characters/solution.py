# LeetCode 0003 - Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last: dict[str, int] = {}
        best = 0
        start = 0

        for i, ch in enumerate(s):
            if ch in last and last[ch] >= start:
                start = last[ch] + 1
            last[ch] = i
            best = max(best, i - start + 1)

        return best
