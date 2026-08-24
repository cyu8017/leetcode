# LeetCode 2578 - Split With Minimum Sum
# https://leetcode.com/problems/split-with-minimum-sum/

class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        digits.sort()
        a = b = 0
        for i, d in enumerate(digits):
            if i % 2 == 0:
                a = a * 10 + d
            else:
                b = b * 10 + d
        return a + b
