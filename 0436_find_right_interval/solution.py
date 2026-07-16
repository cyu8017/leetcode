# LeetCode 0436 - Find Right Interval
# https://leetcode.com/problems/find-right-interval/

import bisect


class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        indexed = sorted((start, index) for index, (start, _) in enumerate(intervals))
        starts = [start for start, _ in indexed]
        result: list[int] = []
        for start, end in intervals:
            position = bisect.bisect_left(starts, end)
            if position == len(starts):
                result.append(-1)
            else:
                result.append(indexed[position][1])
        return result
