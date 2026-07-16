# LeetCode 1146 - Snapshot Array
# https://leetcode.com/problems/snapshot-array/

import bisect


class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.data = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        hist = self.data[index]
        if hist[-1][0] == self.snap_id:
            hist[-1] = (self.snap_id, val)
        else:
            hist.append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        hist = self.data[index]
        i = bisect.bisect_right(hist, (snap_id, float("inf"))) - 1
        return hist[i][1]
