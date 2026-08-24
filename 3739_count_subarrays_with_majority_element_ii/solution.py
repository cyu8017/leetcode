# LeetCode 3739 - Count Subarrays With Majority Element II
# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

from typing import List


class BIT:
    def __init__(self, n_: int) -> None:
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
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        tree = BIT(2 * n + 1)
        s = n + 1
        tree.update(s, 1)
        ans = 0
        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1
            ans += tree.query(s - 1)
            tree.update(s, 1)
        return ans
