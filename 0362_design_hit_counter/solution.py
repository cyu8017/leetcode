# LeetCode 0362 - Design Hit Counter
# https://leetcode.com/problems/design-hit-counter/

from collections import deque


class HitCounter:
    def __init__(self):
        self.hits: deque[int] = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)
