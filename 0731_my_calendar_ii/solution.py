# LeetCode 0731 - My Calendar II
# https://leetcode.com/problems/my-calendar-ii/


class MyCalendarTwo:
    def __init__(self):
        self.booked: list[tuple[int, int]] = []
        self.overlaps: list[tuple[int, int]] = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.overlaps:
            if start < endTime and startTime < end:
                return False
        for start, end in self.booked:
            if start < endTime and startTime < end:
                self.overlaps.append((max(start, startTime), min(end, endTime)))
        self.booked.append((startTime, endTime))
        return True
