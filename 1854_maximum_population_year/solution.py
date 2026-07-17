# LeetCode 1854 - Maximum Population Year
# https://leetcode.com/problems/maximum-population-year/

from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        diff = [0] * 101

        for birth, death in logs:
            diff[birth - 1950] += 1
            diff[death - 1950] -= 1

        best_year = 1950
        best_population = 0
        population = 0

        for offset in range(101):
            population += diff[offset]
            if population > best_population:
                best_population = population
                best_year = 1950 + offset

        return best_year
