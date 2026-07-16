from typing import List

from collections import deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        positions = [deque() for _ in range(10)]
        for i, ch in enumerate(s):
            positions[int(ch)].append(i)
        for ch in t:
            d = int(ch)
            if not positions[d]:
                return False
            index = positions[d][0]
            if any(positions[smaller] and positions[smaller][0] < index for smaller in range(d)):
                return False
            positions[d].popleft()
        return True
