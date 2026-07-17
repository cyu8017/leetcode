# LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def min_side_sum(value: int, count: int) -> int:
            if value > count:
                return (value - 1 + value - count) * count // 2
            return value * (value - 1) // 2 + (count - value + 1)

        lo, hi = 1, maxSum
        while lo < hi:
            mid = (lo + hi + 1) // 2
            total = (
                min_side_sum(mid, index)
                + mid
                + min_side_sum(mid, n - index - 1)
            )
            if total <= maxSum:
                lo = mid
            else:
                hi = mid - 1
        return lo
