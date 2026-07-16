from typing import List, Optional

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int],
                verticalCuts: List[int]) -> int:
        hs = sorted([0, h] + horizontalCuts)
        vs = sorted([0, w] + verticalCuts)
        return max(b-a for a, b in zip(hs, hs[1:])) * max(b-a for a, b in zip(vs, vs[1:])) % 1_000_000_007
