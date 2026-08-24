# LeetCode 3959 - Check Good Integer
# https://leetcode.com/problems/check-good-integer/


class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s = 0
        while n > 0:
            x = n % 10
            s += x * (x - 1)
            n //= 10
        return s >= 50
