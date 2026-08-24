# LeetCode 3489 - Zero Array Transformation IV
# https://leetcode.com/problems/zero-array-transformation-iv/

from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def can_subset_sum(vals: List[int], target: int) -> bool:
            if target == 0:
                return True
            dp = [False] * (target + 1)
            dp[0] = True
            for v in vals:
                for s in range(target, v - 1, -1):
                    if dp[s - v]:
                        dp[s] = True
            return dp[target]

        def ok(k: int) -> bool:
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                vals = []
                for q in range(k):
                    l, r, v = queries[q]
                    if l <= i <= r:
                        vals.append(v)
                if not can_subset_sum(vals, nums[i]):
                    return False
            return True

        if ok(0):
            return 0
        lo, hi = 1, len(queries) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid <= len(queries) and ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return -1 if lo > len(queries) else lo
