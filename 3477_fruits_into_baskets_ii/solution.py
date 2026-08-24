# LeetCode 3477 - Fruits Into Baskets II
# https://leetcode.com/problems/fruits-into-baskets-ii/

from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False] * len(baskets)
        unplaced = 0
        for f in fruits:
            placed = False
            for j in range(len(baskets)):
                if not used[j] and baskets[j] >= f:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced
