# LeetCode 2249 - Count Lattice Points Inside a Circle
# https://leetcode.com/problems/count-lattice-points-inside-a-circle/

from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        seen = set()
        for x, y, r in circles:
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i - x) * (i - x) + (j - y) * (j - y) <= r * r:
                        seen.add((i, j))
        return len(seen)
