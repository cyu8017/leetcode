# LeetCode 3457 - Eat Pizzas!
# https://leetcode.com/problems/eat-pizzas/

from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas = sorted(pizzas)
        n = len(pizzas)
        days = n // 4
        ans = 0
        odd_days = (days + 1) // 2
        even_days = days // 2
        idx = n - 1
        for _ in range(odd_days):
            ans += pizzas[idx]
            idx -= 1
        for _ in range(even_days):
            idx -= 1
            ans += pizzas[idx]
            idx -= 1
        return ans
