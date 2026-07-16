# LeetCode 0706 - Design HashMap
# https://leetcode.com/problems/design-hashmap/


class MyHashMap:
    def __init__(self):
        self.data: dict[int, int] = {}

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data.get(key, -1)

    def remove(self, key: int) -> None:
        self.data.pop(key, None)
