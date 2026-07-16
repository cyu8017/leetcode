# LeetCode 0492 - Construct the Rectangle
# https://leetcode.com/problems/construct-the-rectangle/

import math


class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        limit = int(math.isqrt(area))
        for width in range(limit, 0, -1):
            if area % width == 0:
                length = area // width
                return [length, width]
        return [area, 1]
