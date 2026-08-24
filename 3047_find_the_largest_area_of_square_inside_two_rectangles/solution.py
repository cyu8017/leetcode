# LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ans = 0
        n = len(bottomLeft)
        for i in range(n):
            x1, y1 = bottomLeft[i][0], bottomLeft[i][1]
            x2, y2 = topRight[i][0], topRight[i][1]
            for j in range(i + 1, n):
                x3, y3 = bottomLeft[j][0], bottomLeft[j][1]
                x4, y4 = topRight[j][0], topRight[j][1]
                ww = min(x2, x4) - max(x1, x3)
                h = min(y2, y4) - max(y1, y3)
                e = min(ww, h)
                if e > 0:
                    ans = max(ans, e * e)
        return ans
