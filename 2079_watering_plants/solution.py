# LeetCode 2079 - Watering Plants
# https://leetcode.com/problems/watering-plants/

from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        cur = capacity
        for i, p in enumerate(plants):
            if cur < p:
                ans += i * 2
                cur = capacity
            cur -= p
            ans += 1
        return ans
