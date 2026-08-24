# LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
# https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

from typing import List


class Fenwick3915:
    def __init__(self, n: int):
        self.f = [0] * n

    def update(self, i: int, val: int) -> None:
        while i < len(self.f):
            self.f[i] = max(self.f[i], val)
            i += i & -i

    def preMax(self, i: int) -> int:
        res = 0
        while i > 0:
            res = max(res, self.f[i])
            i &= i - 1
        return res


class Solution:
    def maxAlternatingSum(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        m = 0
        for i in range(len(sorted_nums)):
            if i == 0 or sorted_nums[i] != sorted_nums[i - 1]:
                sorted_nums[m] = sorted_nums[i]
                m += 1
        sorted_nums = sorted_nums[:m]
        n = len(nums)
        f_inc = [0] * n
        f_dec = [0] * n
        inc = Fenwick3915(m + 1)
        dec = Fenwick3915(m + 1)
        ans = 0
        ranks = [0] * n
        for i in range(n):
            x = nums[i]
            if i >= k:
                j = ranks[i - k]
                inc.update(m - j, f_inc[i - k])
                dec.update(j + 1, f_dec[i - k])
            lo = 0
            hi = len(sorted_nums)
            while lo < hi:
                mid = (lo + hi) >> 1
                if sorted_nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            ranks[i] = lo
            f_inc[i] = dec.preMax(lo) + x
            f_dec[i] = inc.preMax(m - 1 - lo) + x
            ans = max(ans, max(f_inc[i], f_dec[i]))
        return ans
