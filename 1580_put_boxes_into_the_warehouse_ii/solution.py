from typing import List

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        n = len(warehouse)
        left, right = warehouse[:], warehouse[:]
        for i in range(1, n):
            left[i] = min(left[i], left[i - 1])
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i], right[i + 1])
        capacity = sorted(max(left[i], right[i]) for i in range(n))
        boxes.sort()
        i = 0
        for room in capacity:
            if i < len(boxes) and boxes[i] <= room:
                i += 1
        return i
