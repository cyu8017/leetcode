# LeetCode 3899 - Angles Of A Triangle
# https://leetcode.com/problems/angles-of-a-triangle/

import math
from typing import List


class Solution:
    def internalAngles(self, sides: List[float]) -> List[float]:
        sides = sorted(sides)
        a, b, c = sides[0], sides[1], sides[2]
        if a + b <= c:
            return []
        pi = math.acos(-1.0)
        A = math.acos((b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / pi
        B = math.acos((a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / pi
        C = 180.0 - A - B
        return [A, B, C]
