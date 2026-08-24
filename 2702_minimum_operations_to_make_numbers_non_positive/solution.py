# LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
# https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

from typing import List
import math


class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        lo, hi = 0, 0
        for v in nums:
            hi = max(hi, math.ceil(v / y), math.ceil(v / x))
        hi += len(nums)

        def ok(ops: int) -> bool:
            extra = 0
            for v in nums:
                remain = v - ops * y
                if remain > 0:
                    extra += math.ceil(remain / (x - y))
            return extra <= ops

        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
