# LeetCode 2626 - Array Reduce Transformation
# https://leetcode.com/problems/array-reduce-transformation/

from typing import Any, Callable, List


class Solution:
    def reduce(self, nums: List[int], fn: Callable, init: Any) -> Any:
        acc = init
        for x in nums:
            acc = fn(acc, x)
        return acc
