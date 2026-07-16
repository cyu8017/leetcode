# LeetCode 0253 - Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(start for start, _ in intervals)
        ends = sorted(end for _, end in intervals)
        rooms = 0
        max_rooms = 0
        start_index = end_index = 0
        while start_index < len(starts):
            if starts[start_index] < ends[end_index]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start_index += 1
            else:
                rooms -= 1
                end_index += 1
        return max_rooms
