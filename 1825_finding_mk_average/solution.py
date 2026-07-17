# LeetCode 1825 - Finding MK Average
# https://leetcode.com/problems/finding-mk-average/

from collections import deque


class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.stream: deque[int] = deque()

    def addElement(self, num: int) -> None:
        self.stream.append(num)

    def calculateMKAverage(self) -> int:
        if len(self.stream) < self.m:
            return -1
        window = sorted(list(self.stream)[-self.m :])
        middle = window[self.k : len(window) - self.k]
        return sum(middle) // len(middle)
