# LeetCode 0759 - Employee Free Time
# https://leetcode.com/problems/employee-free-time/

from typing import List, Union


class Interval:
    def __init__(self, start: int = 0, end: int = 0):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(
        self, schedule: List[List[Union[Interval, List[int]]]]
    ) -> List[List[int]]:
        intervals: list[list[int]] = []
        for employee in schedule:
            for item in employee:
                if isinstance(item, list):
                    intervals.append([item[0], item[1]])
                else:
                    intervals.append([item.start, item.end])

        intervals.sort(key=lambda iv: iv[0])
        merged: list[list[int]] = []
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return [[merged[i - 1][1], merged[i][0]] for i in range(1, len(merged))]
