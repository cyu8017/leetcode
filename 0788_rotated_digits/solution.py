# LeetCode 0788 - Rotated Digits
# https://leetcode.com/problems/rotated-digits/


class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = set("0125689")
        changing = set("2569")
        count = 0
        for num in range(1, n + 1):
            s = str(num)
            if set(s) <= valid and any(ch in changing for ch in s):
                count += 1
        return count
