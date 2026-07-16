# LeetCode 1040 - Moving Stones Until Consecutive II
# https://leetcode.com/problems/moving-stones-until-consecutive-ii/

class Solution:
    def numMovesStonesII(self, stones: list[int]) -> list[int]:
        stones.sort()
        n = len(stones)
        max_moves = max(
            stones[-1] - stones[1] - n + 2,
            stones[-2] - stones[0] - n + 2,
        )
        min_moves = max_moves
        i = 0
        for j in range(n):
            while stones[j] - stones[i] + 1 > n:
                i += 1
            inside = j - i + 1
            if inside == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - inside)
        return [min_moves, max_moves]
