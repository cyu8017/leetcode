# LeetCode 2544 - Alternating Digit Sum
# https://leetcode.com/problems/alternating-digit-sum/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = []
        x = n
        while x > 0:
            digits.append(x % 10)
            x //= 10
        ans = 0
        sign = 1
        for i in range(len(digits) - 1, -1, -1):
            ans += sign * digits[i]
            sign = -sign
        return ans
