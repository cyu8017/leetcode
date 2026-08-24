# LeetCode 3675 - Minimum Operations to Transform String
# https://leetcode.com/problems/minimum-operations-to-transform-string/


class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        for c in s:
            if c != "a":
                ans = max(ans, 26 - (ord(c) - 97))
        return ans
