# LeetCode 2631 - Group By
# https://leetcode.com/problems/group-by/

from typing import Any, Callable, Dict, List


class Solution:
    def groupBy(self, array: List[Any], fn: Callable) -> Dict[Any, List[Any]]:
        out = {}
        for x in array:
            k = fn(x)
            if k not in out:
                out[k] = []
            out[k].append(x)
        return out
