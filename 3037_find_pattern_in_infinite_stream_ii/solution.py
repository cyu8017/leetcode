# LeetCode 3037 - Find Pattern in Infinite Stream II
# https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

from typing import List


def getLPS(pattern: List[int]) -> List[int]:
    n = len(pattern)
    lps = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and pattern[j] != pattern[i]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps


class Solution:
    def findPattern(self, stream, pattern: List[int]) -> int:
        lps = getLPS(pattern)
        i = 0
        j = 0
        bit = 0
        readNext = False
        while True:
            if not readNext:
                bit = stream.next()
                readNext = True
            if bit == pattern[j]:
                i += 1
                readNext = False
                j += 1
                if j == len(pattern):
                    return i - j
            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1
                readNext = False
