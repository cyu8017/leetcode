# LeetCode 0385 - Mini Parser
# https://leetcode.com/problems/mini-parser/


class NestedInteger:
    def __init__(self, value: int | None = None):
        self._integer = value
        self._list: list["NestedInteger"] = []

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int:
        return self._integer if self._integer is not None else 0

    def getList(self) -> list["NestedInteger"]:
        return self._list


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":
            return NestedInteger(int(s))

        stack: list[NestedInteger] = []
        current: NestedInteger | None = None
        index = 0
        negative = False
        number = 0
        has_number = False

        while index < len(s):
            char = s[index]
            if char == "[":
                item = NestedInteger()
                if current is not None:
                    stack.append(current)
                current = item
            elif char == "-":
                negative = True
            elif char.isdigit():
                number = number * 10 + int(char)
                has_number = True
            elif char in ",]":
                if has_number:
                    value = -number if negative else number
                    current.getList().append(NestedInteger(value))
                    number = 0
                    negative = False
                    has_number = False
                if char == "]":
                    if not stack:
                        return current
                    parent = stack.pop()
                    parent.getList().append(current)
                    current = parent
            index += 1

        return current if current is not None else NestedInteger()
