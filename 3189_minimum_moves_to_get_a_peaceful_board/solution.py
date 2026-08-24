# LeetCode 3189 - Minimum Moves to Get a Peaceful Board
# https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

from typing import List


class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        ans = 0
        rooks.sort(key=lambda a: a[0])
        for i in range(len(rooks)):
            ans += abs(rooks[i][0] - i)
        rooks.sort(key=lambda a: a[1])
        for j in range(len(rooks)):
            ans += abs(rooks[j][1] - j)
        return ans
