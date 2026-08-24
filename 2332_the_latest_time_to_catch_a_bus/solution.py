# LeetCode 2332 - The Latest Time to Catch a Bus
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

from typing import List


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses = sorted(buses)
        passengers = sorted(passengers)
        pos = 0
        for bi, bus in enumerate(buses):
            cap = capacity
            while cap > 0 and pos < len(passengers) and passengers[pos] <= bus:
                pos += 1
                cap -= 1
            if bi == len(buses) - 1:
                cand = bus
                if cap == 0:
                    cand = passengers[pos - 1]
                taken = set(passengers)
                while cand in taken:
                    cand -= 1
                return cand
        return -1
