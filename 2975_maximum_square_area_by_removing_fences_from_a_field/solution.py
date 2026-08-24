# LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

from typing import List, Set


def gaps(fences: List[int], bound: int) -> Set[int]:
    lst = [1] + fences + [bound]
    lst.sort()
    g = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            g.add(lst[j] - lst[i])
    return g


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 1000000007
        hg = gaps(hFences, m)
        vg = gaps(vFences, n)
        best = -1
        for g in hg:
            if g in vg and g > best:
                best = g
        if best < 0:
            return -1
        return best * best % mod
