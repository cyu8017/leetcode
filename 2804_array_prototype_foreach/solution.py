# LeetCode 2804 - Array Prototype ForEach
# https://leetcode.com/problems/array-prototype-foreach/

from typing import Any, Callable, List, Optional


class Solution:
    def forEach(self, arr: List[Any], callback: Callable, context: Optional[Any] = None) -> None:
        for i, val in enumerate(arr):
            if context is None:
                callback(val, i, arr)
            else:
                callback(val, i, arr)
