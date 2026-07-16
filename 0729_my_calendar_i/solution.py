# LeetCode 0729 - My Calendar I
# https://leetcode.com/problems/my-calendar-i/


class MyCalendar:
    def __init__(self):
        self.bookings: list[tuple[int, int]] = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.bookings:
            if start < endTime and startTime < end:
                return False
        self.bookings.append((startTime, endTime))
        return True
