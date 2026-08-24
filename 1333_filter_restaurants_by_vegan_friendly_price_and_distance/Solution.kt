// LeetCode 1333 - Filter Restaurants by Vegan-Friendly, Price and Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

class Solution {
    fun filterRestaurants(
        restaurants: Array<IntArray>,
        veganFriendly: Int,
        maxPrice: Int,
        maxDistance: Int
    ): List<Int> {
        return restaurants
            .filter { row ->
                (veganFriendly == 0 || row[2] == 1) &&
                    row[3] <= maxPrice &&
                    row[4] <= maxDistance
            }
            .sortedWith(compareByDescending<IntArray> { it[1] }.thenByDescending { it[0] })
            .map { it[0] }
    }
}
