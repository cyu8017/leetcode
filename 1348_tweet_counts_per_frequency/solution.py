# LeetCode 1348 - Tweet Counts Per Frequency

from bisect import bisect_left, bisect_right, insort
from collections import defaultdict
from typing import List

class TweetCounts:
    def __init__(self):
        self.times = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        insort(self.times[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        size = {"minute": 60, "hour": 3600, "day": 86400}[freq]
        times = self.times[tweetName]
        answer = []
        for start in range(startTime, endTime + 1, size):
            end = min(endTime, start + size - 1)
            answer.append(bisect_right(times, end) - bisect_left(times, start))
        return answer
