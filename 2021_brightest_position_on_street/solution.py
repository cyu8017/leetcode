# LeetCode 2021 - Brightest Position on Street
# https://leetcode.com/problems/brightest-position-on-street/

from typing import List


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        events = []
        for pos, r in lights:
            events.append((pos - r, 1))
            events.append((pos + r + 1, -1))
        events.sort(key=lambda e: (e[0], -e[1]))
        best = 0
        cur = 0
        ans = 0
        for pos, d in events:
            cur += d
            if cur > best:
                best = cur
                ans = pos
        return ans
