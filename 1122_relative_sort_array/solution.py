# LeetCode 1122 - Relative Sort Array
# https://leetcode.com/problems/relative-sort-array/

from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        count = Counter(arr1)
        ans: list[int] = []
        for x in arr2:
            ans.extend([x] * count.pop(x, 0))
        for x in sorted(count):
            ans.extend([x] * count[x])
        return ans
