# LeetCode 3498 - Reverse Degree of a String
# https://leetcode.com/problems/reverse-degree-of-a-string/


class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            ans += (26 - (ord(c) - 97)) * (i + 1)
        return ans
