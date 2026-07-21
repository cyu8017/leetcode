from typing import List
import math

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = sorted(math.ceil(d / s) for d, s in zip(dist, speed))
        for i, t in enumerate(arrival):
            if t <= i:
                return i
        return len(arrival)
