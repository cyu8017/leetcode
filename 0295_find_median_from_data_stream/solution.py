# LeetCode 0295 - Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

import heapq


class MedianFinder:
    def __init__(self):
        self.small: list[int] = []
        self.large: list[int] = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
