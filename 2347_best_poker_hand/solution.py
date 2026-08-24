# LeetCode 2347 - Best Poker Hand
# https://leetcode.com/problems/best-poker-hand/

from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
            return "Flush"
        cnt = {}
        best = 0
        for r in ranks:
            c = cnt.get(r, 0) + 1
            cnt[r] = c
            best = max(best, c)
        if best >= 3:
            return "Three of a Kind"
        if best == 2:
            return "Pair"
        return "High Card"
