# LeetCode 0435 - Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        removed = 0
        end = float("-inf")
        for start, finish in intervals:
            if start < end:
                removed += 1
            else:
                end = finish
        return removed
