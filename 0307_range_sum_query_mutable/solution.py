# LeetCode 0307 - Range Sum Query - Mutable
# https://leetcode.com/problems/range-sum-query-mutable/

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(nums)
        self.tree = [0] * (self.size + 1)

        def add(index: int, delta: int) -> None:
            while index <= self.size:
                self.tree[index] += delta
                index += index & -index

        for index, value in enumerate(nums):
            add(index + 1, value)

        self._add = add

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        def prefix(index: int) -> int:
            total = 0
            while index > 0:
                total += self.tree[index]
                index -= index & -index
            return total

        return prefix(right + 1) - prefix(left)
