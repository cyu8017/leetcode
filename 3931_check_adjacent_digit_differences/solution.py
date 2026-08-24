# LeetCode 3931 - Check Adjacent Digit Differences
# https://leetcode.com/problems/check-adjacent-digit-differences/


class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(1, len(s)):
            if abs(ord(s[i - 1]) - ord(s[i])) > 2:
                return False
        return True
