# LeetCode 3407 - Substring Matching Pattern
# https://leetcode.com/problems/substring-matching-pattern/


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        i = p.find("*")
        left = p[:i]
        right = p[i + 1 :]
        li = s.find(left)
        if li < 0:
            return False
        return s.find(right, li + len(left)) >= 0
