# LeetCode 1326 - Minimum Number Of Taps To Open To Water A Garden

from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        farthest = [0] * (n + 1)
        for center, radius in enumerate(ranges):
            left, right = max(0, center - radius), min(n, center + radius)
            farthest[left] = max(farthest[left], right)
        taps = end = reach = 0
        for position in range(n):
            reach = max(reach, farthest[position])
            if position == end:
                if reach <= position:
                    return -1
                taps += 1
                end = reach
        return taps
