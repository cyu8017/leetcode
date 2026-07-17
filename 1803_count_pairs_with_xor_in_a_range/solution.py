# LeetCode 1803 - Count Pairs With XOR in a Range
# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/


class TrieNode:
    __slots__ = ("count", "children")

    def __init__(self) -> None:
        self.count = 0
        self.children: list[TrieNode | None] = [None, None]


class Solution:
    def countPairs(self, nums: list[int], low: int, high: int) -> int:
        return self._count_smaller_than(nums, high + 1) - self._count_smaller_than(nums, low)

    def _count_smaller_than(self, nums: list[int], limit: int) -> int:
        if limit <= 0:
            return 0

        root = TrieNode()
        total = 0
        max_bit = 15

        for num in nums:
            total += self._query(root, num, limit, max_bit)
            self._insert(root, num, max_bit)
        return total

    def _insert(self, root: TrieNode, num: int, bit: int) -> None:
        node = root
        for i in range(bit, -1, -1):
            b = (num >> i) & 1
            if node.children[b] is None:
                node.children[b] = TrieNode()
            node = node.children[b]
            node.count += 1

    def _query(self, root: TrieNode, num: int, limit: int, bit: int) -> int:
        if root is None or bit < 0:
            return 0

        num_bit = (num >> bit) & 1
        limit_bit = (limit >> bit) & 1
        child = root.children[num_bit]

        if limit_bit == 1:
            result = child.count if child else 0
            result += self._query(root.children[1 - num_bit], num, limit, bit - 1)
            return result
        return self._query(child, num, limit, bit - 1)
