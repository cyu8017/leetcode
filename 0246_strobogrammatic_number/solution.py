# LeetCode 0246 - Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        left, right = 0, len(num) - 1
        while left <= right:
            if mapping.get(num[left]) != num[right]:
                return False
            left += 1
            right -= 1
        return True
