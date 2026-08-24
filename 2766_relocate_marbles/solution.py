# LeetCode 2766 - Relocate Marbles
# https://leetcode.com/problems/relocate-marbles/

from typing import List


class Solution:
    def relocateMarbles(
        self, nums: List[int], moveFrom: List[int], moveTo: List[int]
    ) -> List[int]:
        pos = set(nums)
        for src, dst in zip(moveFrom, moveTo):
            pos.discard(src)
            pos.add(dst)
        return sorted(pos)
