# LeetCode 0339 - Nested List Weight Sum
# https://leetcode.com/problems/nested-list-weight-sum/

from typing import List


class NestedInteger:
    def __init__(self, value: int | None = None):
        self._integer = value
        self._list: list["NestedInteger"] = []

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int:
        return self._integer if self._integer is not None else 0

    def getList(self) -> List["NestedInteger"]:
        return self._list


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        total = 0

        def dfs(items: List[NestedInteger], depth: int) -> None:
            nonlocal total
            for item in items:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    dfs(item.getList(), depth + 1)

        dfs(nestedList, 1)
        return total
