# LeetCode 3279 - Maximum Total Area Occupied by Pistons
# https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

from typing import List


class Solution:
    def maxArea(self, height: int, positions: List[int], directions: str) -> int:
        n = len(positions)
        pos = positions[:]
        dirc = list(directions)
        best = 0
        for t in range(2 * height + 1):
            s = 0
            for i in range(n):
                s += pos[i]
            if s > best:
                best = s
            for i in range(n):
                if dirc[i] == "U":
                    if pos[i] == height:
                        dirc[i] = "D"
                        pos[i] -= 1
                    else:
                        pos[i] += 1
                else:
                    if pos[i] == 0:
                        dirc[i] = "U"
                        pos[i] += 1
                    else:
                        pos[i] -= 1
        return best
