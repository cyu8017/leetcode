# LeetCode 2695 - Array Wrapper
# https://leetcode.com/problems/array-wrapper/

from typing import List


class ArrayWrapper:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def valueOf(self) -> int:
        s = 0
        for x in self.nums:
            s += x
        return s

    def __add__(self, other: "ArrayWrapper") -> int:
        return self.valueOf() + other.valueOf()

    def __int__(self) -> int:
        return self.valueOf()

    def toString(self) -> str:
        return "[" + ",".join(str(x) for x in self.nums) + "]"

    def __str__(self) -> str:
        return self.toString()


class Solution:
    def ArrayWrapper(self, nums: List[int]) -> ArrayWrapper:
        return ArrayWrapper(nums)
