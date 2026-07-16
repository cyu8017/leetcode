# LeetCode 0149 - Max Points on a Line
# https://leetcode.com/problems/max-points-on-a-line/

from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        best = 1
        for i in range(n):
            slopes: dict[tuple[int, int], int] = defaultdict(int)
            local = 1
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slopes[(dx, dy)] += 1
                local = max(local, slopes[(dx, dy)] + 1)
            best = max(best, local)
        return best
