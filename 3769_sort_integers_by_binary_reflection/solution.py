# LeetCode 3769 - Sort Integers by Binary Reflection
# https://leetcode.com/problems/sort-integers-by-binary-reflection/

from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def f(x: int) -> int:
            y = 0
            while x != 0:
                y = (y << 1) | (x & 1)
                x >>= 1
            return y

        arr = nums[:]
        arr.sort(key=lambda a: (f(a), a))
        for i in range(len(nums)):
            nums[i] = arr[i]
        return nums
