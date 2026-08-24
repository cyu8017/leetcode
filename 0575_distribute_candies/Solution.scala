// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/

object Solution {
  def distributeCandies(candyType: Array[Int]): Int = {
    val unique = candyType.toSet
    math.min(unique.size, candyType.length / 2)
  }
}
