# LeetCode 1891 - Cutting Ribbons
# https://leetcode.com/problems/cutting-ribbons/

class Solution:
    def maxLength(self, ribbons: list[int], k: int) -> int:
        def can(length: int) -> bool:
            return sum(ribbon // length for ribbon in ribbons) >= k

        lo, hi = 1, max(ribbons)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo if can(lo) else 0
