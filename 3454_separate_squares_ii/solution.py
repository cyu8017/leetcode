# LeetCode 3454 - Separate Squares II
# https://leetcode.com/problems/separate-squares-ii/

from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        for sq in squares:
            l = sq[2]
            total += l * l

        def area_below(y: float) -> float:
            below = 0.0
            for sq in squares:
                yi, l = sq[1], sq[2]
                top = yi + l
                if y <= yi:
                    continue
                elif y >= top:
                    below += l * l
                else:
                    below += l * (y - yi)
            return below

        lo, hi = 0.0, 2e9
        for _ in range(60):
            mid = (lo + hi) / 2
            if area_below(mid) * 2 < total:
                lo = mid
            else:
                hi = mid
        return hi
