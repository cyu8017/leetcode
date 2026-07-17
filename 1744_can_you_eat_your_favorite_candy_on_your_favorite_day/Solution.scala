// LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
// https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

object Solution {
  def canEat(candiesCount: Array[Int], queries: Array[Array[Int]]): Array[Boolean] = {
    val prefix = new Array[Long](candiesCount.length + 1)
    for (i <- candiesCount.indices) {
      prefix(i + 1) = prefix(i) + candiesCount(i)
    }
    queries.map { query =>
      val candyType = query(0)
      val day = query(1).toLong
      val cap = query(2).toLong
      val minEaten = day + 1
      val maxEaten = (day + 1) * cap
      maxEaten > prefix(candyType) && minEaten <= prefix(candyType + 1)
    }
  }
}
