# LeetCode 3288 - Length of the Longest Increasing Path
# https://leetcode.com/problems/length-of-the-longest-increasing-path/

from typing import List


def lis(a: List[int]) -> int:
    tails = []
    for x in a:
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) >> 1
            if tails[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(tails):
            tails.append(x)
        else:
            tails[lo] = x
    return len(tails)


class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        arr = [[coordinates[i][0], coordinates[i][1], i] for i in range(n)]
        arr.sort(key=lambda a: (a[0], -a[1]))
        kx, ky = coordinates[k][0], coordinates[k][1]
        left, right = [], []
        for p in arr:
            if p[0] < kx and p[1] < ky:
                left.append(p[1])
            if p[0] > kx and p[1] > ky:
                right.append(p[1])
        return lis(left) + 1 + lis(right)
