# LeetCode 2619 - Array Prototype Last
# https://leetcode.com/problems/array-prototype-last/

from typing import Any, List


class Solution:
    def last(self, nums: List[Any]) -> Any:
        if len(nums) == 0:
            return -1
        return nums[-1]
