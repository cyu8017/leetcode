# LeetCode 3975 - Filter Occupied Intervals
# https://leetcode.com/problems/filter-occupied-intervals/

from typing import List


class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals.sort(key=lambda a: a[0])
        busy = [[occupiedIntervals[0][0], occupiedIntervals[0][1]]]
        for i in range(1, len(occupiedIntervals)):
            cur = occupiedIntervals[i]
            last = busy[-1]
            if last[1] + 1 < cur[0]:
                busy.append([cur[0], cur[1]])
            elif cur[1] > last[1]:
                last[1] = cur[1]
        ans = []
        for it in busy:
            s, e = it[0], it[1]
            if e < freeStart or s > freeEnd:
                ans.append([s, e])
            else:
                if s < freeStart:
                    ans.append([s, freeStart - 1])
                if e > freeEnd:
                    ans.append([freeEnd + 1, e])
        return ans
