# LeetCode 3746 - Minimum String Length After Balanced Removals
# https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a = sum(1 for ch in s if ch == "a")
        b = len(s) - a
        return abs(a - b)
