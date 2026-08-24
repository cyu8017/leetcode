# LeetCode 3023 - Find Pattern in Infinite Stream I
# https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

from typing import List


class Solution:
    def findPattern(self, stream, pattern: List[int]) -> int:
        a = 0
        b = 0
        m = len(pattern)
        half = m >> 1
        mask1 = (1 << half) - 1
        mask2 = (1 << (m - half)) - 1
        for i in range(half):
            a |= pattern[i] << (half - 1 - i)
        for i in range(half, m):
            b |= pattern[i] << (m - 1 - i)
        x = 0
        y = 0
        i = 1
        while True:
            v = stream.next()
            y = y << 1 | v
            v = (y >> (m - half)) & 1
            y &= mask2
            x = x << 1 | v
            x &= mask1
            if i >= m and a == x and b == y:
                return i - m
            i += 1
