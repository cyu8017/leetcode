# LeetCode 3259 - Maximum Energy Boost From Two Drinks
# https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

from typing import List


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dpA = [0] * n
        dpB = [0] * n
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]
        if n == 1:
            return max(dpA[0], dpB[0])
        dpA[1] = energyDrinkA[1] + dpA[0]
        dpB[1] = energyDrinkB[1] + dpB[0]
        for i in range(2, n):
            dpA[i] = energyDrinkA[i] + max(dpA[i - 1], dpB[i - 2])
            dpB[i] = energyDrinkB[i] + max(dpB[i - 1], dpA[i - 2])
        return max(dpA[n - 1], dpB[n - 1])
