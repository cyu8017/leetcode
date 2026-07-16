# LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/


class RandomizedCollection:
    def __init__(self):
        self.values: list[int] = []
        self.indices: dict[int, set[int]] = {}

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            self.indices[val] = set()
        self.indices[val].add(len(self.values))
        self.values.append(val)
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.indices or not self.indices[val]:
            return False

        index = next(iter(self.indices[val]))
        last_index = len(self.values) - 1
        last_value = self.values[last_index]
        self.values[index] = last_value
        self.indices[last_value].discard(last_index)
        self.indices[last_value].add(index)
        self.values.pop()
        self.indices[val].discard(index)
        if not self.indices[val]:
            del self.indices[val]
        return True

    def getRandom(self) -> int:
        return self.values[-1]
