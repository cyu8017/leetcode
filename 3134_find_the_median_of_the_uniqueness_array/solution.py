# LeetCode 3134 - Find the Median of the Uniqueness Array
# https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

from typing import List


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        m = (1 + n) * n // 2

        def check(mx: int) -> bool:
            cnt = {}
            l = 0
            k = 0
            for r in range(n):
                cnt[nums[r]] = cnt.get(nums[r], 0) + 1
                while len(cnt) > mx:
                    y = nums[l]
                    l += 1
                    nv = cnt[y] - 1
                    if nv == 0:
                        del cnt[y]
                    else:
                        cnt[y] = nv
                k += r - l + 1
                if k >= (m + 1) // 2:
                    return True
            return False

        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
