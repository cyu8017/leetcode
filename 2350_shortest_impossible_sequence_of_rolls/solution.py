# LeetCode 2350 - Shortest Impossible Sequence of Rolls
# https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

from typing import List


class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        ans = 1
        for r in rolls:
            seen.add(r)
            if len(seen) == k:
                ans += 1
                seen.clear()
        return ans
