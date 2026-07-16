from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        owned, opened = set(initialBoxes), set()
        queue = deque(box for box in initialBoxes if status[box])
        total = 0
        while queue:
            box = queue.popleft()
            if box in opened or not status[box]:
                continue
            opened.add(box)
            total += candies[box]
            for key in keys[box]:
                status[key] = 1
                if key in owned and key not in opened:
                    queue.append(key)
            for child in containedBoxes[box]:
                owned.add(child)
                if status[child] and child not in opened:
                    queue.append(child)
        return total
