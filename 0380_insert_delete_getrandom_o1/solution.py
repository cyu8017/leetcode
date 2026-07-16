# LeetCode 0380 - Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/


class RandomizedSet:
    def __init__(self):
        self.values: list[int] = []
        self.index_by_value: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.index_by_value:
            return False
        self.index_by_value[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_by_value:
            return False

        index = self.index_by_value[val]
        last_value = self.values[-1]
        self.values[index] = last_value
        self.index_by_value[last_value] = index
        self.values.pop()
        del self.index_by_value[val]
        return True

    def getRandom(self) -> int:
        return self.values[-1]
