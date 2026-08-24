# LeetCode 3111 - Minimum Rectangles to Cover Points
# https://leetcode.com/problems/minimum-rectangles-to-cover-points/

from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points = sorted(points, key=lambda p: p[0])
        ans = 0
        x1 = -1
        for p in points:
            if p[0] > x1:
                ans += 1
                x1 = p[0] + w
        return ans
