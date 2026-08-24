# LeetCode 3768 - Minimum Inversion Count in Subarrays of Fixed Length
# https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

from typing import List


class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        vals = sorted(nums)
        n = 0
        for i in range(len(vals)):
            if n == 0 or vals[i] != vals[n - 1]:
                vals[n] = vals[i]
                n += 1
        vals = vals[:n]
        bit = [0] * (len(vals) + 1)

        def add(i: int, delta: int) -> None:
            while i < len(bit):
                bit[i] += delta
                i += i & -i

        def sum(i: int) -> int:
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def lowerBound(a: List[int], x: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        rank = [0] * len(nums)
        inv = 0
        for i in range(len(nums)):
            rank[i] = lowerBound(vals, nums[i]) + 1
            if i < k:
                inv += i - sum(rank[i])
                add(rank[i], 1)
        best = inv
        for r in range(k, len(nums)):
            left = rank[r - k]
            inv -= sum(left - 1)
            add(left, -1)
            inv += k - 1 - sum(rank[r])
            add(rank[r], 1)
            if inv < best:
                best = inv
        return best
