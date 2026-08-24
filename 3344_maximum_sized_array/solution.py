# LeetCode 3344 - Maximum Sized Array
# https://leetcode.com/problems/maximum-sized-array/


def ok(n: int, s: int) -> bool:
    total = 0
    for i in range(n):
        for j in range(n):
            ij = i | j
            total += ij * (n - 1) * n // 2
            if total > s:
                return False
    return total <= s


class Solution:
    def maxSizedArray(self, s: int) -> int:
        lo, hi = 1, 2000
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid, s):
                lo = mid
            else:
                hi = mid - 1
        return lo
