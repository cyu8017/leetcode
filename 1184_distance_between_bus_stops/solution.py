# LeetCode 1184 - Distance Between Bus Stops
# https://leetcode.com/problems/distance-between-bus-stops/

class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        clockwise = sum(distance[start:destination])
        return min(clockwise, sum(distance) - clockwise)
