# LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can(x: int) -> bool:
            need = 0
            for q in quantities:
                need += (q + x - 1) // x
                if need > n:
                    return False
            return True

        lo, hi = 1, max(quantities)
        while lo < hi:
            mid = (lo + hi) >> 1
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
