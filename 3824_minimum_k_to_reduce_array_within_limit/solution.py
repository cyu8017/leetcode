# LeetCode 3824 - Minimum K to Reduce Array Within Limit
# https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

from typing import List


def check(nums: List[int], k: int) -> bool:
    t = 0
    for x in nums:
        t += (x + k - 1) // k
    return t <= k * k


class Solution:
    def minimumK(self, nums: List[int]) -> int:
        lo, hi = 1, 100000
        while lo < hi:
            mid = (lo + hi) // 2
            if check(nums, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
