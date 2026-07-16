from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        lo, hi = 0, max(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(min(x, mid) for x in arr) < target:
                lo = mid + 1
            else:
                hi = mid
        before = sum(min(x, lo - 1) for x in arr)
        after = sum(min(x, lo) for x in arr)
        return lo - 1 if target - before <= after - target else lo
