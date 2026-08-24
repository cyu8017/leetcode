# LeetCode 3369 - Design an Array Statistics Tracker
# https://leetcode.com/problems/design-an-array-statistics-tracker/


class StatisticsTracker:
    def __init__(self) -> None:
        self.arr = []
        self.sum = 0
        self.freq = {}
        self.modeFreq = 0
        self.modes = set()

    def addNumber(self, num: int) -> None:
        self.arr.append(num)
        self.sum += num
        f = self.freq.get(num, 0) + 1
        self.freq[num] = f
        if f > self.modeFreq:
            self.modeFreq = f
            self.modes.clear()
            self.modes.add(num)
        elif f == self.modeFreq:
            self.modes.add(num)

    def removeFirst(self) -> None:
        if not self.arr:
            return
        num = self.arr.pop(0)
        self.sum -= num
        f = self.freq[num] - 1
        if f == 0:
            del self.freq[num]
        else:
            self.freq[num] = f
        self.modeFreq = 0
        self.modes.clear()
        for v, ff in self.freq.items():
            if ff > self.modeFreq:
                self.modeFreq = ff
                self.modes.clear()
                self.modes.add(v)
            elif ff == self.modeFreq:
                self.modes.add(v)

    def getMean(self) -> int:
        if not self.arr:
            return 0
        return self.sum // len(self.arr)

    def getMedian(self) -> int:
        n = len(self.arr)
        tmp = sorted(self.arr)
        if n % 2 == 1:
            return tmp[n // 2]
        return tmp[n // 2 - 1]

    def getMode(self) -> int:
        best = 9007199254740991
        for v in self.modes:
            if v < best:
                best = v
        if best == 9007199254740991:
            return 0
        return best
