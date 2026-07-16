# LeetCode 0514 - Freedom Trail
# https://leetcode.com/problems/freedom-trail/

from functools import lru_cache


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        positions: dict[str, list[int]] = {}
        for index, char in enumerate(ring):
            positions.setdefault(char, []).append(index)

        @lru_cache(maxsize=None)
        def dp(ring_index: int, key_index: int) -> int:
            if key_index == len(key):
                return 0
            best = float("inf")
            for pos in positions[key[key_index]]:
                clockwise = (pos - ring_index) % len(ring)
                counter = (ring_index - pos) % len(ring)
                steps = min(clockwise, counter) + 1
                best = min(best, steps + dp(pos, key_index + 1))
            return best

        return dp(0, 0)
