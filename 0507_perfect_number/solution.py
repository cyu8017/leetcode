# LeetCode 0507 - Perfect Number
# https://leetcode.com/problems/perfect-number/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        total = 1
        limit = int(num**0.5)
        for divisor in range(2, limit + 1):
            if num % divisor == 0:
                total += divisor
                pair = num // divisor
                if pair != divisor:
                    total += pair
        return total == num
