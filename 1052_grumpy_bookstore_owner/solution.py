# LeetCode 1052 - Grumpy Bookstore Owner
# https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)
        gain = best = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            if g:
                gain += c
            if i >= minutes and grumpy[i - minutes]:
                gain -= customers[i - minutes]
            best = max(best, gain)
        return base + best
