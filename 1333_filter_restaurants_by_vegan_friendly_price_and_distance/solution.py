# LeetCode 1333 - Filter Restaurants By Vegan Friendly Price And Distance

from typing import List

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        valid = [row for row in restaurants
                 if (not veganFriendly or row[2]) and row[3] <= maxPrice and row[4] <= maxDistance]
        valid.sort(key=lambda row: (row[1], row[0]), reverse=True)
        return [row[0] for row in valid]
