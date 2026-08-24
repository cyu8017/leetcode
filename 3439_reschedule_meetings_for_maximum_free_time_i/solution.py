# LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        gaps[n] = eventTime - endTime[n - 1]
        window = k + 1
        s = 0
        for i in range(min(window, len(gaps))):
            s += gaps[i]
        ans = s
        for i in range(window, len(gaps)):
            s += gaps[i] - gaps[i - window]
            if s > ans:
                ans = s
        return ans
