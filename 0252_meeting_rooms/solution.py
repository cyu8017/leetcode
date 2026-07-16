# LeetCode 0252 - Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda interval: interval[0])
        for index in range(1, len(intervals)):
            if intervals[index][0] < intervals[index - 1][1]:
                return False
        return True
