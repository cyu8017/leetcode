# LeetCode 2353 - Design a Food Rating System
# https://leetcode.com/problems/design-a-food-rating-system/

from typing import List


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisineOf = {}
        self.ratingOf = {}
        self.heaps = {}
        for i in range(len(foods)):
            self.cuisineOf[foods[i]] = cuisines[i]
            self.ratingOf[foods[i]] = ratings[i]
            if cuisines[i] not in self.heaps:
                self.heaps[cuisines[i]] = []
            self.heaps[cuisines[i]].append(foods[i])

    def _cmp(self, a: str, b: str) -> int:
        ra, rb = self.ratingOf[a], self.ratingOf[b]
        if ra != rb:
            return rb - ra
        if a < b:
            return -1
        if a > b:
            return 1
        return 0

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratingOf[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        foods = self.heaps[cuisine]
        foods.sort(key=lambda x: (-self.ratingOf[x], x))
        return foods[0]
