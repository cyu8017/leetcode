# LeetCode 0871 - Minimum Number of Refueling Stops
# https://leetcode.com/problems/minimum-number-of-refueling-stops/

import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        pq: list[int] = []
        stations.append([target, 0])
        ans = prev = 0
        fuel = startFuel
        for pos, gas in stations:
            fuel -= pos - prev
            while pq and fuel < 0:
                fuel += -heapq.heappop(pq)
                ans += 1
            if fuel < 0:
                return -1
            heapq.heappush(pq, -gas)
            prev = pos
        return ans
