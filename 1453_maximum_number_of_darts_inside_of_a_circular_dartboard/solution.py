from typing import List, Optional

import math

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        ans = 1 if darts else 0
        for i, (x1, y1) in enumerate(darts):
            for x2, y2 in darts[i + 1:]:
                dx, dy = x2 - x1, y2 - y1
                d2 = dx * dx + dy * dy
                if d2 > 4 * r * r or d2 == 0:
                    continue
                d = math.sqrt(d2)
                h = math.sqrt(r * r - d2 / 4)
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                for sign in (-1, 1):
                    cx = mx + sign * (-dy) * h / d
                    cy = my + sign * dx * h / d
                    ans = max(ans, sum((x - cx) ** 2 + (y - cy) ** 2 <= r * r + 1e-7
                                       for x, y in darts))
        return ans
