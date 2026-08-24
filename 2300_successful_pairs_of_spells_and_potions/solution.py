# LeetCode 2300 - Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = [0] * len(spells)
        for i, spell in enumerate(spells):
            lo, hi = 0, m
            while lo < hi:
                mid = (lo + hi) >> 1
                if spell * potions[mid] >= success:
                    hi = mid
                else:
                    lo = mid + 1
            ans[i] = m - lo
        return ans
