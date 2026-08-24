# LeetCode 3468 - Find the Number of Copy Arrays
# https://leetcode.com/problems/find-the-number-of-copy-arrays/

from typing import List


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)
        lo, hi = bounds[0][0], bounds[0][1]
        for i in range(1, n):
            diff = original[i] - original[i - 1]
            lo2, hi2 = bounds[i][0], bounds[i][1]
            nlo, nhi = lo + diff, hi + diff
            if nlo < lo2:
                nlo = lo2
            if nhi > hi2:
                nhi = hi2
            if nlo > nhi:
                return 0
            lo, hi = nlo, nhi
        return hi - lo + 1
