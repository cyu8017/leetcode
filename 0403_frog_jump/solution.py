# LeetCode 0403 - Frog Jump
# https://leetcode.com/problems/frog-jump/

from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        jumps: dict[int, set[int]] = {stone: set() for stone in stones}
        jumps[0].add(0)

        for stone in stones:
            for jump in jumps[stone]:
                for next_jump in (jump - 1, jump, jump + 1):
                    if next_jump > 0 and stone + next_jump in stone_set:
                        jumps[stone + next_jump].add(next_jump)

        return bool(jumps[stones[-1]])
