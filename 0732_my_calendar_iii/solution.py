# LeetCode 0732 - My Calendar III
# https://leetcode.com/problems/my-calendar-iii/


class MyCalendarThree:
    def __init__(self):
        self.delta: dict[int, int] = {}

    def book(self, startTime: int, endTime: int) -> int:
        self.delta[startTime] = self.delta.get(startTime, 0) + 1
        self.delta[endTime] = self.delta.get(endTime, 0) - 1
        current = best = 0
        for time in sorted(self.delta):
            current += self.delta[time]
            best = max(best, current)
        return best
