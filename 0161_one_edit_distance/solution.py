# LeetCode 0161 - One Edit Distance
# https://leetcode.com/problems/one-edit-distance/


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        if len(s) > len(t):
            s, t = t, s
        i = 0
        while i < len(s) and s[i] == t[i]:
            i += 1
        if len(s) == len(t):
            return s[i + 1 :] == t[i + 1 :]
        return s[i:] == t[i + 1 :]
