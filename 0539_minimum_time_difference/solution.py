# LeetCode 0539 - Minimum Time Difference
# https://leetcode.com/problems/minimum-time-difference/

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            hour, minute = map(int, time.split(":"))
            minutes.append(hour * 60 + minute)

        minutes.sort()
        best = minutes[-1] - minutes[0]
        for i in range(1, len(minutes)):
            best = min(best, minutes[i] - minutes[i - 1])
        return min(best, 24 * 60 - minutes[-1] + minutes[0])
