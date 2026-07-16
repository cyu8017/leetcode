# LeetCode 1134 - Armstrong Number
# https://leetcode.com/problems/armstrong-number/

class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = str(n)
        power = len(digits)
        return n == sum(int(d) ** power for d in digits)
