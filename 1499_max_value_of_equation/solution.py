from typing import List, Optional

from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q, ans = deque(), -10**20
        for x, y in points:
            while q and x - q[0][0] > k:
                q.popleft()
            if q:
                ans = max(ans, x + y + q[0][1])
            value = y - x
            while q and q[-1][1] <= value:
                q.pop()
            q.append((x, value))
        return ans
