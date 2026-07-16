# LeetCode 0904 - Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count: dict[int, int] = defaultdict(int)
        left = ans = 0
        for right, kind in enumerate(fruits):
            count[kind] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
