# LeetCode 2363 - Merge Similar Items
# https://leetcode.com/problems/merge-similar-items/

from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        mp = {}
        for it in items1:
            mp[it[0]] = mp.get(it[0], 0) + it[1]
        for it in items2:
            mp[it[0]] = mp.get(it[0], 0) + it[1]
        return [[k, v] for k, v in sorted(mp.items())]
