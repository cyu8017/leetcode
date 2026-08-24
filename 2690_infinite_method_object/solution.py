# LeetCode 2690 - Infinite Method Object
# https://leetcode.com/problems/infinite-method-object/

from typing import Any, Callable


class _InfiniteObject:
    def __getattr__(self, name: str) -> Callable[..., str]:
        return lambda *args, **kwargs: "Hello World"


class Solution:
    def createInfiniteObject(self) -> Any:
        return _InfiniteObject()
