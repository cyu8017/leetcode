# LeetCode 3270 - Find the Key of the Numbers
# https://leetcode.com/problems/find-the-key-of-the-numbers/

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans, mul = 0, 1
        for t in range(4):
            d = min(num1 % 10, num2 % 10, num3 % 10)
            ans += d * mul
            mul *= 10
            num1 //= 10
            num2 //= 10
            num3 //= 10
        return ans
