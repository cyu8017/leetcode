# LeetCode 0757 - Set Intersection Size At Least Two
# https://leetcode.com/problems/set-intersection-size-at-least-two/

from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[1], interval[0]))
        size = 0
        first = second = -1
        for left, right in intervals:
            if left <= first:
                continue
            if left <= second:
                size += 1
                first, second = second, right
            else:
                size += 2
                first, second = right - 1, right
        return size
