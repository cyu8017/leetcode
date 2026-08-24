# LeetCode 2418 - Sort the People
# https://leetcode.com/problems/sort-the-people/

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        idx = list(range(n))
        idx.sort(key=lambda i: -heights[i])
        return [names[i] for i in idx]
