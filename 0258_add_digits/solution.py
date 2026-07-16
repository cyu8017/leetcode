# LeetCode 0258 - Add Digits
# https://leetcode.com/problems/add-digits/


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
