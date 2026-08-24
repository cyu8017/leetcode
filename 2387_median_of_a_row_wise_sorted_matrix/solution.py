# LeetCode 2387 - Median of a Row Wise Sorted Matrix
# https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

from typing import List


class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        lo, hi = 1, 1000000
        need = (m * n) // 2 + 1

        def count_le(x: int) -> int:
            cnt = 0
            for row in grid:
                l, r = 0, n
                while l < r:
                    mid = (l + r) >> 1
                    if row[mid] <= x:
                        l = mid + 1
                    else:
                        r = mid
                cnt += l
            return cnt

        while lo < hi:
            mid = (lo + hi) >> 1
            if count_le(mid) >= need:
                hi = mid
            else:
                lo = mid + 1
        return lo
