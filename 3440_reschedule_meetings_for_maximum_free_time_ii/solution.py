# LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        gaps[n] = eventTime - endTime[n - 1]
        ans = 0
        for g in gaps:
            if g > ans:
                ans = g
        left_max = [0] * (n + 1)
        right_max = [0] * (n + 1)
        for i in range(n + 1):
            left_max[i] = gaps[i]
            if i > 0 and left_max[i - 1] > left_max[i]:
                left_max[i] = left_max[i - 1]
        for i in range(n, -1, -1):
            right_max[i] = gaps[i]
            if i < n and right_max[i + 1] > right_max[i]:
                right_max[i] = right_max[i + 1]
        for i in range(n):
            dur = endTime[i] - startTime[i]
            merged = gaps[i] + gaps[i + 1]
            best_other = 0
            if i > 0 and left_max[i - 1] > best_other:
                best_other = left_max[i - 1]
            if i + 2 <= n and right_max[i + 2] > best_other:
                best_other = right_max[i + 2]
            cand = merged
            if best_other >= dur:
                cand = merged + dur
            if cand > ans:
                ans = cand
        return ans
