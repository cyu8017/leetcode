# LeetCode 3316 - Find Maximum Removals From Source String
# https://leetcode.com/problems/find-maximum-removals-from-source-string/

from typing import List


def ok(removeFirst: int, source: str, pattern: str, targetIndices: List[int], n: int) -> bool:
    mark = [False] * n
    for i in range(removeFirst):
        mark[targetIndices[i]] = True
    j = 0
    i = 0
    while i < n and j < len(pattern):
        if not mark[i] and source[i] == pattern[j]:
            j += 1
        i += 1
    return j == len(pattern)


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        n = len(source)
        lo, hi = 0, len(targetIndices)
        while lo < hi:
            mid = (lo + hi + 1) >> 1
            if ok(mid, source, pattern, targetIndices, n):
                lo = mid
            else:
                hi = mid - 1
        return lo
