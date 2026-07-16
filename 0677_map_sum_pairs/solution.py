# LeetCode 0677 - Map Sum Pairs
# https://leetcode.com/problems/map-sum-pairs/


class MapSum:
    def __init__(self):
        self.values: dict[str, int] = {}
        self.prefix_sums: dict[str, int] = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.values.get(key, 0)
        self.values[key] = val
        for i in range(1, len(key) + 1):
            prefix = key[:i]
            self.prefix_sums[prefix] = self.prefix_sums.get(prefix, 0) + delta

    def sum(self, prefix: str) -> int:
        return self.prefix_sums.get(prefix, 0)
