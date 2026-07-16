# LeetCode 0575 - Distribute Candies
# https://leetcode.com/problems/distribute-candies/

from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)
