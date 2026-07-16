# LeetCode 0900 - RLE Iterator
# https://leetcode.com/problems/rle-iterator/

class RLEIterator:
    def __init__(self, encoding: list[int]):
        self.enc = encoding
        self.i = 0

    def next(self, n: int) -> int:
        while self.i < len(self.enc):
            if self.enc[self.i] >= n:
                self.enc[self.i] -= n
                return self.enc[self.i + 1]
            n -= self.enc[self.i]
            self.i += 2
        return -1
