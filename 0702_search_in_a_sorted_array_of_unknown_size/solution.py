# LeetCode 0702 - Search in a Sorted Array of Unknown Size
# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

from typing import List, Protocol, Union


class ArrayReader(Protocol):
    def get(self, index: int) -> int: ...


class _ListReader:
    def __init__(self, secret: List[int]):
        self.secret = secret

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.secret):
            return 2**31 - 1
        return self.secret[index]


class Solution:
    def search(self, reader: Union[ArrayReader, List[int]], target: int) -> int:
        if isinstance(reader, list):
            reader = _ListReader(reader)

        right = 1
        while reader.get(right) < target:
            right <<= 1
        left = right >> 1

        while left <= right:
            mid = (left + right) // 2
            value = reader.get(mid)
            if value == target:
                return mid
            if value > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
