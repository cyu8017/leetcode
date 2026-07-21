from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        prev = 0
        ans = 0
        for r in rungs:
            gap = r - prev
            if gap > dist:
                ans += (gap - 1) // dist
            prev = r
        return ans
