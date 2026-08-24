# LeetCode 3394 - Check if Grid can be Cut into Sections
# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

from typing import List


def checkCut(rects: List[List[int]], axis: int) -> bool:
    arr = [[r[0], r[2]] if axis == 0 else [r[1], r[3]] for r in rects]
    arr.sort(key=lambda x: (x[0], x[1]))
    cuts = 0
    end = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][0] >= end:
            cuts += 1
            end = arr[i][1]
            if cuts >= 2:
                return True
        elif arr[i][1] > end:
            end = arr[i][1]
    return False


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return checkCut(rectangles, 0) or checkCut(rectangles, 1)
