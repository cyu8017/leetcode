# LeetCode 0389 - Find the Difference
# https://leetcode.com/problems/find-the-difference/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor_value = 0
        for char in s + t:
            xor_value ^= ord(char)
        return chr(xor_value)
