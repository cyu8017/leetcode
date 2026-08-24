# LeetCode 3460 - Longest Common Prefix After at Most One Removal
# https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/


class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        i = j = 0
        removed = False
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            if removed:
                break
            removed = True
            i += 1
        return j
