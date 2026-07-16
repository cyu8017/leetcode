# LeetCode 0352 - Data Stream as Disjoint Intervals
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/

from typing import List


class SummaryRanges:
    def __init__(self):
        self.intervals: list[list[int]] = []

    def addNum(self, value: int) -> None:
        new_interval = [value, value]
        merged: list[list[int]] = []
        inserted = False

        for interval in self.intervals:
            if interval[1] < value - 1:
                merged.append(interval)
            elif interval[0] > value + 1:
                if not inserted:
                    merged.append(new_interval)
                    inserted = True
                merged.append(interval)
            else:
                new_interval[0] = min(new_interval[0], interval[0])
                new_interval[1] = max(new_interval[1], interval[1])

        if not inserted:
            merged.append(new_interval)

        self.intervals = merged

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
