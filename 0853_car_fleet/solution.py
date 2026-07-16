# LeetCode 0853 - Car Fleet
# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        max_time = 0.0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets
