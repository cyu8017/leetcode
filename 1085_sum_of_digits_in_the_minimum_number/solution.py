# LeetCode 1085 - Sum of Digits in the Minimum Number
# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

class Solution:
    def sumOfDigits(self, nums: list[int]) -> int:
        n = min(nums)
        digit_sum = 0
        while n:
            digit_sum += n % 10
            n //= 10
        return 0 if digit_sum % 2 else 1
