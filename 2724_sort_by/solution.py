# LeetCode 2724 - Sort By
# https://leetcode.com/problems/sort-by/

from typing import Any, Callable, List


class Solution:
    def sortBy(self, arr: List[Any], fn: Callable[[Any], Any]) -> List[Any]:
        return sorted(arr, key=fn)
