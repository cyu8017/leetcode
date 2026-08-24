# LeetCode 3096 - Minimum Levels to Gain More Points
# https://leetcode.com/problems/minimum-levels-to-gain-more-points/

from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        s = 0
        for x in possible:
            s += -1 if x == 0 else x
        t = 0
        for i in range(len(possible) - 1):
            x = -1 if possible[i] == 0 else possible[i]
            t += x
            if t > s - t:
                return i + 1
        return -1
