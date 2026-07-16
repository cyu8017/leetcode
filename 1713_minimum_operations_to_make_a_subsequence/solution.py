from bisect import bisect_left
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        pos = {value: i for i, value in enumerate(target)}
        lis = []
        for value in arr:
            if value not in pos:
                continue
            idx = pos[value]
            place = bisect_left(lis, idx)
            if place == len(lis):
                lis.append(idx)
            else:
                lis[place] = idx
        return len(target) - len(lis)
