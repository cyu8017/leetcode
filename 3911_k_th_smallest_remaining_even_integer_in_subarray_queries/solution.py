# LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
# https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

from typing import List


def UpperBound3911(a: List[int], x: int) -> int:
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def kthSmallestEven(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        even_prefix = [0] * (n + 1)
        for i in range(n):
            even_prefix[i + 1] = even_prefix[i] + (1 if nums[i] % 2 == 0 else 0)
        ans = [0] * len(queries)
        for qi in range(len(queries)):
            l, r = queries[qi][0], queries[qi][1]
            k = queries[qi][2]
            lo = 1
            hi = k + (r - l + 1)
            while lo < hi:
                mid = (lo + hi) // 2
                pos = UpperBound3911(nums, 2 * mid)
                if pos > r + 1:
                    pos = r + 1
                removed = 0
                if pos > l:
                    removed = even_prefix[pos] - even_prefix[l]
                if mid - removed >= k:
                    hi = mid
                else:
                    lo = mid + 1
            ans[qi] = 2 * lo
        return ans
