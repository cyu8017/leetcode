class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        return [value + extraCandies >= maximum for value in candies]
