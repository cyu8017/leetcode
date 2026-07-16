# LeetCode 0364 - Nested List Weight Sum II
# https://leetcode.com/problems/nested-list-weight-sum-ii/

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
        weighted: list[tuple[int, int]] = []

        def dfs(items: List[NestedInteger], depth: int) -> None:
            for item in items:
                if item.isInteger():
                    weighted.append((item.getInteger(), depth))
                else:
                    dfs(item.getList(), depth + 1)

        dfs(nestedList, 1)
        if not weighted:
            return 0

        max_depth = max(depth for _, depth in weighted)
        return sum(value * (max_depth - depth + 1) for value, depth in weighted)
