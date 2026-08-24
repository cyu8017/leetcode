# LeetCode 2250 - Count Number of Rectangles Containing Each Point
# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

from typing import List


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        by_h = [[] for _ in range(101)]
        for x, h in rectangles:
            by_h[h].append(x)
        for h in range(1, 101):
            by_h[h].sort()
        ans = [0] * len(points)
        for i, (x, y) in enumerate(points):
            cnt = 0
            for h in range(y, 101):
                xs = by_h[h]
                lo, hi = 0, len(xs)
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if xs[mid] < x:
                        lo = mid + 1
                    else:
                        hi = mid
                cnt += len(xs) - lo
            ans[i] = cnt
        return ans
