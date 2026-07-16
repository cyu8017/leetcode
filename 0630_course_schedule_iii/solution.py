# LeetCode 0630 - Course Schedule III
# https://leetcode.com/problems/course-schedule-iii/

import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])
        heap: list[int] = []
        time = 0

        for duration, last_day in courses:
            if time + duration <= last_day:
                heapq.heappush(heap, -duration)
                time += duration
            elif heap and -heap[0] > duration:
                time += duration + heapq.heappop(heap)
                heapq.heappush(heap, -duration)

        return len(heap)
