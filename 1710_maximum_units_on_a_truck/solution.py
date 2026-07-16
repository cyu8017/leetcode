from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total = 0
        for count, units in sorted(boxTypes, key=lambda item: -item[1]):
            take = min(count, truckSize)
            total += take * units
            truckSize -= take
            if truckSize == 0:
                break
        return total
