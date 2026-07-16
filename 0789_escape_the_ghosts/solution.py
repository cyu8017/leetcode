# LeetCode 0789 - Escape The Ghosts
# https://leetcode.com/problems/escape-the-ghosts/

from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        target_dist = abs(target[0]) + abs(target[1])
        return all(
            abs(gx - target[0]) + abs(gy - target[1]) > target_dist
            for gx, gy in ghosts
        )
