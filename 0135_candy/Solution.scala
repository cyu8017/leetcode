// LeetCode 0135 - Candy
// https://leetcode.com/problems/candy/

object Solution {
  def candy(ratings: Array[Int]): Int = {
    val candies = Array.fill(ratings.length)(1)
    for (i <- 1 until ratings.length if ratings(i) > ratings(i - 1)) candies(i) = candies(i - 1) + 1
    for (i <- (ratings.length - 2) to 0 by -1 if ratings(i) > ratings(i + 1)) candies(i) = math.max(candies(i), candies(i + 1) + 1)
    candies.sum
  }
}
