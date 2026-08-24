# LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
# https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

from typing import List


class Solution:
    def minInitialStrength(self, monsters: List[int], boosts: List[List[int]]) -> int:
        n = len(monsters)
        d = [0] * (n + 1)
        for b in boosts:
            d[b[0]] += b[2]
            d[b[1] + 1] -= b[2]
        left = 0
        right = 1000000000000000
        while left < right:
            mid = (left + right) // 2
            if self.check(mid, monsters, d):
                right = mid
            else:
                left = mid + 1
        return left

    def check(self, v: int, monsters: List[int], d: List[int]) -> bool:
        bonus = 0
        for i in range(len(monsters)):
            bonus += d[i]
            if v + bonus < monsters[i]:
                return False
            v -= monsters[i]
            if v < 0:
                v = 0
        return True
