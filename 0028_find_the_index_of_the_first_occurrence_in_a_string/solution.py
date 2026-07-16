# LeetCode 0028 - Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):
            if haystack[i : i + needle_len] == needle:
                return i

        return -1
