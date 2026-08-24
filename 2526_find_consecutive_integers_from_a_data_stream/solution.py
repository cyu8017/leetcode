# LeetCode 2526 - Find Consecutive Integers from a Data Stream
# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/


class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.streak = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.streak += 1
        else:
            self.streak = 0
        return self.streak >= self.k
