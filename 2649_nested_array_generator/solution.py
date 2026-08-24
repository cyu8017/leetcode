# LeetCode 2649 - Nested Array Generator
# https://leetcode.com/problems/nested-array-generator/

from typing import Any, Generator, List, Union


class Solution:
    def inorderTraversal(self, arr: List[Any]) -> Generator[Any, None, None]:
        for x in arr:
            if isinstance(x, list):
                yield from self.inorderTraversal(x)
            else:
                yield x
