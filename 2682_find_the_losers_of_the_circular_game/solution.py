# LeetCode 2682 - Find the Losers of the Circular Game
# https://leetcode.com/problems/find-the-losers-of-the-circular-game/

from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = [False] * (n + 1)
        cur, step = 1, 1
        while not seen[cur]:
            seen[cur] = True
            cur = (cur - 1 + step * k) % n + 1
            step += 1
        return [i for i in range(1, n + 1) if not seen[i]]
