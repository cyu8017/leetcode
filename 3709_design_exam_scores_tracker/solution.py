# LeetCode 3709 - Design Exam Scores Tracker
# https://leetcode.com/problems/design-exam-scores-tracker/

import bisect


class ExamTracker:
    def __init__(self) -> None:
        self.times = [0]
        self.pre = [0]

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.pre.append(self.pre[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        l = bisect.bisect_left(self.times, startTime) - 1
        r = bisect.bisect_left(self.times, endTime + 1) - 1
        return self.pre[r] - self.pre[l]
