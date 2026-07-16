# LeetCode 0855 - Exam Room
# https://leetcode.com/problems/exam-room/

import bisect


class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.seats: list[int] = []

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        best_seat = 0
        best_dist = self.seats[0]
        for i in range(1, len(self.seats)):
            dist = (self.seats[i] - self.seats[i - 1]) // 2
            if dist > best_dist:
                best_dist = dist
                best_seat = self.seats[i - 1] + dist
        if self.n - 1 - self.seats[-1] > best_dist:
            best_seat = self.n - 1
        bisect.insort(self.seats, best_seat)
        return best_seat

    def leave(self, p: int) -> None:
        self.seats.remove(p)
