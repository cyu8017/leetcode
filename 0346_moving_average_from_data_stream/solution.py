# LeetCode 0346 - Moving Average from Data Stream
# https://leetcode.com/problems/moving-average-from-data-stream/

from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.values: deque[int] = deque()
        self.total = 0

    def next(self, val: int) -> float:
        self.values.append(val)
        self.total += val
        if len(self.values) > self.size:
            self.total -= self.values.popleft()
        return self.total / len(self.values)
