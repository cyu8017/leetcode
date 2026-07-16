# LeetCode 0705 - Design HashSet
# https://leetcode.com/problems/design-hashset/


class MyHashSet:
    def __init__(self):
        self.data: set[int] = set()

    def add(self, key: int) -> None:
        self.data.add(key)

    def remove(self, key: int) -> None:
        self.data.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.data
