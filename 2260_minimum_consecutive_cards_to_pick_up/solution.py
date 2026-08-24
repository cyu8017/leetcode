# LeetCode 2260 - Minimum Consecutive Cards to Pick Up
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last = {}
        ans = -1
        for i, x in enumerate(cards):
            if x in last:
                diff = i - last[x] + 1
                if ans == -1 or diff < ans:
                    ans = diff
            last[x] = i
        return ans
