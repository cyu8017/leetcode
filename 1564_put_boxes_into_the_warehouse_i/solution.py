from typing import List

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i - 1])
        boxes.sort()
        room, used = len(warehouse) - 1, 0
        for box in boxes:
            while room >= 0 and warehouse[room] < box:
                room -= 1
            if room < 0:
                break
            used += 1
            room -= 1
        return used
