# LeetCode 2303 - Calculate Amount Paid in Taxes
# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0.0
        prev = 0
        for upper, percent in brackets:
            if income <= prev:
                break
            taxable = income - prev if income < upper else upper - prev
            ans += taxable * percent / 100.0
            prev = upper
        return ans
