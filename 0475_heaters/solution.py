# LeetCode 0475 - Heaters
# https://leetcode.com/problems/heaters/

import bisect


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()
        radius = 0
        for house in houses:
            position = bisect.bisect_left(heaters, house)
            distances: list[int] = []
            if position < len(heaters):
                distances.append(abs(heaters[position] - house))
            if position > 0:
                distances.append(abs(heaters[position - 1] - house))
            radius = max(radius, min(distances))
        return radius
