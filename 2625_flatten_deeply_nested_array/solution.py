# LeetCode 2625 - Flatten Deeply Nested Array
# https://leetcode.com/problems/flatten-deeply-nested-array/

from typing import Any, List


class Solution:
    def flat(self, arr: List[Any], n: int) -> List[Any]:
        res = []

        def dfs(a: List[Any], depth: int) -> None:
            for x in a:
                if isinstance(x, list) and depth < n:
                    dfs(x, depth + 1)
                else:
                    res.append(x)

        dfs(arr, 0)
        return res
