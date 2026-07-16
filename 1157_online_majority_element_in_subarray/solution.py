# LeetCode 1157 - Online Majority Element In Subarray
# https://leetcode.com/problems/online-majority-element-in-subarray/

import bisect
from collections import defaultdict


class MajorityChecker:
    def __init__(self, arr: list[int]):
        self.arr = arr
        self.pos: dict[int, list[int]] = defaultdict(list)
        for i, x in enumerate(arr):
            self.pos[x].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        candidate = count = 0
        for i in range(left, right + 1):
            if count == 0:
                candidate = self.arr[i]
            count += 1 if self.arr[i] == candidate else -1
        locs = self.pos[candidate]
        freq = bisect.bisect_right(locs, right) - bisect.bisect_left(locs, left)
        return candidate if freq >= threshold else -1
