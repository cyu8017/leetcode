# LeetCode 3907 - Count Smaller Elements With Opposite Parity
# https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

from typing import List


class BIT3907:
    def __init__(self, n_: int):
        self.n = n_
        self.c = [0] * (n_ + 1)

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s


class Solution:
    def countSmallerOppositeParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sorted_nums = sorted(nums)
        m = 0
        for i in range(len(sorted_nums)):
            if i == 0 or sorted_nums[i] != sorted_nums[i - 1]:
                sorted_nums[m] = sorted_nums[i]
                m += 1
        sorted_nums = sorted_nums[:m]
        bits = [BIT3907(m), BIT3907(m)]
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            lo = 0
            hi = len(sorted_nums)
            while lo < hi:
                mid = (lo + hi) >> 1
                if sorted_nums[mid] < nums[i]:
                    lo = mid + 1
                else:
                    hi = mid
            x = lo + 1
            ans[i] = bits[(nums[i] & 1) ^ 1].query(x - 1)
            bits[nums[i] & 1].update(x, 1)
        return ans
