# LeetCode 3074 - Apple Redistribution into Boxes
# https://leetcode.com/problems/apple-redistribution-into-boxes/

from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        s = 0
        for x in apple:
            s += x
        i = 1
        while True:
            s -= capacity[len(capacity) - i]
            if s <= 0:
                return i
            i += 1
