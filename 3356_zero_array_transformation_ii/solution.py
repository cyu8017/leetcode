# LeetCode 3356 - Zero Array Transformation II
# https://leetcode.com/problems/zero-array-transformation-ii/

from typing import List


def ok(k: int, nums: List[int], queries: List[List[int]], n: int) -> bool:
    diff = [0] * (n + 1)
    for i in range(k):
        q = queries[i]
        diff[q[0]] += q[2]
        diff[q[1] + 1] -= q[2]
    cur = 0
    for i in range(n):
        cur += diff[i]
        if cur < nums[i]:
            return False
    return True


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        if ok(0, nums, queries, n):
            return 0
        lo, hi = 1, len(queries) + 1
        while lo < hi:
            mid = (lo + hi) >> 1
            if mid <= len(queries) and ok(mid, nums, queries, n):
                hi = mid
            else:
                lo = mid + 1
        if lo > len(queries):
            return -1
        return lo
