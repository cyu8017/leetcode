// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

class FoodRatings(_foods: Array[String], _cuisines: Array[String], _ratings: Array[Int]) {
  private val cuisineOf = scala.collection.mutable.Map.empty[String, String]
  private val ratingOf = scala.collection.mutable.Map.empty[String, Int]
  private val heaps = scala.collection.mutable.Map.empty[String, scala.collection.mutable.TreeSet[(Int, String)]]

  {
    var i = 0
    while (i < _foods.length) {
      cuisineOf(_foods(i)) = _cuisines(i)
      ratingOf(_foods(i)) = _ratings(i)
      heaps.getOrElseUpdate(_cuisines(i), scala.collection.mutable.TreeSet.empty[(Int, String)]) += ((-_ratings(i), _foods(i)))
      i += 1
    }
  }

  def changeRating(food: String, newRating: Int): Unit = {
    val cuisine = cuisineOf(food)
    val set = heaps(cuisine)
    set -= ((-ratingOf(food), food))
    ratingOf(food) = newRating
    set += ((-newRating, food))
  }

  def highestRated(cuisine: String): String = heaps(cuisine).head._2
}
