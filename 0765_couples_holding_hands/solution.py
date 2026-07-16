# LeetCode 0765 - Couples Holding Hands
# https://leetcode.com/problems/couples-holding-hands/

from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {person: index for index, person in enumerate(row)}
        swaps = 0
        for i in range(0, len(row), 2):
            partner = row[i] ^ 1
            if row[i + 1] == partner:
                continue
            j = pos[partner]
            pos[row[i + 1]] = j
            row[j] = row[i + 1]
            row[i + 1] = partner
            pos[partner] = i + 1
            swaps += 1
        return swaps
