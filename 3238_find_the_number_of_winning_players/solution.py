# LeetCode 3238 - Find the Number of Winning Players
# https://leetcode.com/problems/find-the-number-of-winning-players/

from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        cnt = [[0] * 11 for _ in range(n)]
        s = set()
        for p in pick:
            x, y = p[0], p[1]
            cnt[x][y] += 1
            if cnt[x][y] > x:
                s.add(x)
        return len(s)
