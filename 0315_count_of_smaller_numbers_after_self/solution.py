# LeetCode 0315 - Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from bisect import bisect_left
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums: list[int] = []
        result: list[int] = []
        for num in reversed(nums):
            index = bisect_left(sorted_nums, num)
            result.append(index)
            sorted_nums.insert(index, num)
        result.reverse()
        return result
