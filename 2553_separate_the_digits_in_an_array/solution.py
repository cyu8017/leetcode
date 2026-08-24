# LeetCode 2553 - Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/

from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            digits = []
            while num > 0:
                digits.append(num % 10)
                num //= 10
            for i in range(len(digits) - 1, -1, -1):
                ans.append(digits[i])
        return ans
