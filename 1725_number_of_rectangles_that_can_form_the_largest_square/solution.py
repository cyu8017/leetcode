from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sides = [min(a, b) for a, b in rectangles]
        best = max(sides)
        return sides.count(best)
