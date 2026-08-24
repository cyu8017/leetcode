# LeetCode 2943 - Maximize Area of Square Hole in Grid
# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

from typing import List


def maxGap(bars: List[int]) -> int:
    if not bars:
        return 1
    bars.sort()
    best = 1
    cur = 1
    for i in range(1, len(bars)):
        if bars[i] == bars[i - 1] + 1:
            cur += 1
        else:
            cur = 1
        if cur > best:
            best = cur
    return best + 1


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        side = maxGap(hBars[:])
        vs = maxGap(vBars[:])
        if vs < side:
            side = vs
        return side * side
