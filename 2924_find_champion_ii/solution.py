# LeetCode 2924 - Find Champion II
# https://leetcode.com/problems/find-champion-ii/

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0] * n
        for e in edges:
            indeg[e[1]] += 1
        ans = -1
        for i in range(n):
            if indeg[i] == 0:
                if ans != -1:
                    return -1
                ans = i
        return ans
