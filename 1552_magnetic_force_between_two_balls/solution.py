from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo, hi = 1, (position[-1] - position[0]) // (m - 1)
        while lo <= hi:
            mid = (lo + hi) // 2
            count, last = 1, position[0]
            for x in position[1:]:
                if x - last >= mid:
                    count, last = count + 1, x
            if count >= m:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
