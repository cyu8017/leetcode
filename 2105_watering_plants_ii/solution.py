# LeetCode 2105 - Watering Plants II
# https://leetcode.com/problems/watering-plants-ii/

from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        i, j = 0, len(plants) - 1
        a, b, ans = capacityA, capacityB, 0
        while i < j:
            if a < plants[i]:
                ans += 1
                a = capacityA
            a -= plants[i]
            i += 1
            if b < plants[j]:
                ans += 1
                b = capacityB
            b -= plants[j]
            j -= 1
        if i == j:
            if a >= b:
                if a < plants[i]:
                    ans += 1
            elif b < plants[i]:
                ans += 1
        return ans
