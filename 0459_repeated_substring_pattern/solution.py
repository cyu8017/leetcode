# LeetCode 0459 - Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled = s + s
        return s in doubled[1:-1]
