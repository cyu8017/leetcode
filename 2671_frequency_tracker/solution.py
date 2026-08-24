# LeetCode 2671 - Frequency Tracker
# https://leetcode.com/problems/frequency-tracker/

from collections import defaultdict


class FrequencyTracker:
    def __init__(self):
        self.freq = defaultdict(int)
        self.count = defaultdict(int)

    def add(self, number: int) -> None:
        old = self.freq[number]
        if old > 0:
            self.count[old] -= 1
        self.freq[number] = old + 1
        self.count[old + 1] += 1

    def deleteOne(self, number: int) -> None:
        old = self.freq[number]
        if old == 0:
            return
        self.count[old] -= 1
        self.freq[number] = old - 1
        if old - 1 > 0:
            self.count[old - 1] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.count[frequency] > 0
