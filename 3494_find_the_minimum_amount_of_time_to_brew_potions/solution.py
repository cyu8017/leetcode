# LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        done = [0] * n
        for j in range(m):
            t = 0
            for i in range(n):
                if done[i] > t:
                    t = done[i]
                t += skill[i] * mana[j]
                done[i] = t
            for i in range(n - 2, -1, -1):
                done[i] = done[i + 1] - skill[i + 1] * mana[j]
        return done[n - 1]
