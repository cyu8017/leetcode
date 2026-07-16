# LeetCode 0715 - Range Module
# https://leetcode.com/problems/range-module/

import bisect


class RangeModule:
    def __init__(self):
        self.intervals: list[list[int]] = []

    def addRange(self, left: int, right: int) -> None:
        new_intervals: list[list[int]] = []
        placed = False
        for start, end in self.intervals:
            if end < left:
                new_intervals.append([start, end])
            elif right < start:
                if not placed:
                    new_intervals.append([left, right])
                    placed = True
                new_intervals.append([start, end])
            else:
                left = min(left, start)
                right = max(right, end)
        if not placed:
            new_intervals.append([left, right])
        self.intervals = new_intervals

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.intervals, [left, float("inf")]) - 1
        if i < 0:
            return False
        return self.intervals[i][0] <= left and right <= self.intervals[i][1]

    def removeRange(self, left: int, right: int) -> None:
        new_intervals: list[list[int]] = []
        for start, end in self.intervals:
            if end <= left or right <= start:
                new_intervals.append([start, end])
            else:
                if start < left:
                    new_intervals.append([start, left])
                if right < end:
                    new_intervals.append([right, end])
        self.intervals = new_intervals
