// LeetCode 1333 - Filter Restaurants by Vegan-Friendly, Price and Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

object Solution {
  def filterRestaurants(
    restaurants: Array[Array[Int]],
    veganFriendly: Int,
    maxPrice: Int,
    maxDistance: Int
  ): List[Int] = {
    restaurants
      .filter(row =>
        (veganFriendly == 0 || row(2) == 1) &&
          row(3) <= maxPrice &&
          row(4) <= maxDistance
      )
      .sortBy(row => (-row(1), -row(0)))
      .map(_(0))
      .toList
  }
}
