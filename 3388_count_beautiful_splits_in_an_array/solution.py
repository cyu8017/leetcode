# LeetCode 3388 - Count Beautiful Splits in an Array
# https://leetcode.com/problems/count-beautiful-splits-in-an-array/

from typing import List


def equal(a: List[int], as_: int, ae: int, b: List[int], bs: int, be: int) -> bool:
    if ae - as_ != be - bs:
        return False
    for i in range(ae - as_):
        if a[as_ + i] != b[bs + i]:
            return False
    return True


class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                ok = False
                if i <= j - i and equal(nums, 0, i, nums, i, i + i):
                    ok = True
                if (not ok) and j - i <= n - j and equal(nums, i, j, nums, j, j + (j - i)):
                    ok = True
                if ok:
                    ans += 1
        return ans
