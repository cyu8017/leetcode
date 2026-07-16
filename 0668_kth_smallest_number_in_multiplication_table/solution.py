# LeetCode 0668 - Kth Smallest Number in Multiplication Table
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_le(x: int) -> int:
            return sum(min(x // row, n) for row in range(1, m + 1))

        lo, hi = 1, m * n
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
