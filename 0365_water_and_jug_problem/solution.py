# LeetCode 0365 - Water and Jug Problem
# https://leetcode.com/problems/water-and-jug-problem/

import math


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target == 0:
            return True
        if x + y < target:
            return False
        return target % math.gcd(x, y) == 0
