# LeetCode 3983 - Subsequence After One Replacement
# https://leetcode.com/problems/subsequence-after-one-replacement/


class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        i0 = 0
        i1 = 0
        j = 0
        while i1 < m and j < n:
            if s[i1] == t[j]:
                i1 += 1
            if i1 < i0 + 1:
                i1 = i0 + 1
            if s[i0] == t[j]:
                i0 += 1
            j += 1
        return i1 == m
