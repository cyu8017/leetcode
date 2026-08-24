# LeetCode 2225 - Find Players With Zero or One Losses
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose = {}
        seen = set()
        for w, l in matches:
            seen.add(w)
            seen.add(l)
            lose[l] = lose.get(l, 0) + 1
        zero, one = [], []
        for p in seen:
            L = lose.get(p, 0)
            if L == 0:
                zero.append(p)
            elif L == 1:
                one.append(p)
        zero.sort()
        one.sort()
        return [zero, one]
