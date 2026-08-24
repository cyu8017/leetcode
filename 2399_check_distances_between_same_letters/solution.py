# LeetCode 2399 - Check Distances Between Same Letters
# https://leetcode.com/problems/check-distances-between-same-letters/

from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first = [-1] * 26
        for i, ch in enumerate(s):
            c = ord(ch) - 97
            if first[c] == -1:
                first[c] = i
            elif i - first[c] - 1 != distance[c]:
                return False
        return True
