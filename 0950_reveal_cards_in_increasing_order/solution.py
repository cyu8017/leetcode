# LeetCode 0950 - Reveal Cards In Increasing Order
# https://leetcode.com/problems/reveal-cards-in-increasing-order/

from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        n = len(deck)
        idx = deque(range(n))
        ans = [0] * n
        for card in deck:
            ans[idx.popleft()] = card
            if idx:
                idx.append(idx.popleft())
        return ans
