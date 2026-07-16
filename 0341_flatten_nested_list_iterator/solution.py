# LeetCode 0341 - Flatten Nested List Iterator
# https://leetcode.com/problems/flatten-nested-list-iterator/

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


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self._stack: list[tuple[NestedInteger, int]] = []
        for item in reversed(nestedList):
            self._stack.append((item, 0))

    def next(self) -> int:
        current, _ = self._stack.pop()
        if current.isInteger():
            return current.getInteger()
        return self._advance(current.getList())

    def hasNext(self) -> bool:
        self._prepare_next()
        return bool(self._stack)

    def _prepare_next(self) -> None:
        while self._stack:
            current, index = self._stack[-1]
            if current.isInteger():
                return
            nested = current.getList()
            if index >= len(nested):
                self._stack.pop()
                continue
            self._stack[-1] = (current, index + 1)
            self._stack.append((nested[index], 0))

    def _advance(self, nested: List[NestedInteger]) -> int:
        for item in reversed(nested):
            self._stack.append((item, 0))
        self._prepare_next()
        current, _ = self._stack.pop()
        if current.isInteger():
            return current.getInteger()
        return self._advance(current.getList())
