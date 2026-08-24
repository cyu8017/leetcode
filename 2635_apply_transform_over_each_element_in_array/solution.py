# LeetCode 2635 - Apply Transform Over Each Element in Array
# https://leetcode.com/problems/apply-transform-over-each-element-in-array/

from typing import Any, Callable, List


class Solution:
    def map(self, arr: List[Any], fn: Callable) -> List[Any]:
        out = [None] * len(arr)
        for i in range(len(arr)):
            out[i] = fn(arr[i], i)
        return out
