# LeetCode 0592 - Fraction Addition and Subtraction
# https://leetcode.com/problems/fraction-addition-and-subtraction/

import math
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r"[+-]?\d+", expression)))
        numerator, denominator = 0, 1

        for i in range(0, len(nums), 2):
            a, b = nums[i], nums[i + 1]
            numerator = numerator * b + a * denominator
            denominator *= b
            g = math.gcd(numerator, denominator)
            numerator //= g
            denominator //= g

        return f"{numerator}/{denominator}"
