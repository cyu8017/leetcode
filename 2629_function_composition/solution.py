# LeetCode 2629 - Function Composition
# https://leetcode.com/problems/function-composition/

from typing import Callable, List


class Solution:
    def compose(self, functions: List[Callable]) -> Callable:
        def wrapped(x):
            for i in range(len(functions) - 1, -1, -1):
                x = functions[i](x)
            return x

        return wrapped
