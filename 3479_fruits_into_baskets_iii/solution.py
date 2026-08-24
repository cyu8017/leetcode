# LeetCode 3479 - Fruits Into Baskets III
# https://leetcode.com/problems/fruits-into-baskets-iii/

from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 1
        while size < n:
            size <<= 1
        tree = [0] * (size * 2)
        for i in range(n):
            tree[size + i] = baskets[i]
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[i * 2], tree[i * 2 + 1])

        def find(node: int, nl: int, nr: int, need: int) -> int:
            if tree[node] < need:
                return -1
            if nl == nr:
                return nl
            mid = (nl + nr) // 2
            left = find(node * 2, nl, mid, need)
            if left != -1:
                return left
            return find(node * 2 + 1, mid + 1, nr, need)

        def update(idx: int) -> None:
            p = size + idx
            tree[p] = -1
            p >>= 1
            while p > 0:
                tree[p] = max(tree[p * 2], tree[p * 2 + 1])
                p >>= 1

        unplaced = 0
        for f in fruits:
            idx = find(1, 0, size - 1, f)
            if idx == -1 or idx >= n:
                unplaced += 1
            else:
                update(idx)
        return unplaced
