# LeetCode 3340 - Check Balanced String
# https://leetcode.com/problems/check-balanced-string/


class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0
        odd = 0
        for i, ch in enumerate(num):
            if i % 2 == 0:
                even += ord(ch) - 48
            else:
                odd += ord(ch) - 48
        return even == odd
