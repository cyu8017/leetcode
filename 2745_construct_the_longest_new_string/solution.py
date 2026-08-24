# LeetCode 2745 - Construct the Longest New String
# https://leetcode.com/problems/construct-the-longest-new-string/


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x < y:
            return (2 * x + 1 + z) * 2
        if y < x:
            return (2 * y + 1 + z) * 2
        return (x + y + z) * 2
