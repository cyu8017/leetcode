# LeetCode 2634 - Filter Elements from Array
# https://leetcode.com/problems/filter-elements-from-array/

from typing import Any, Callable, List


class Solution:
    def filter(self, arr: List[Any], fn: Callable) -> List[Any]:
        out = []
        for i in range(len(arr)):
            if fn(arr[i], i):
                out.append(arr[i])
        return out
