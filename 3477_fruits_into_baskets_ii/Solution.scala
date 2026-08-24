// LeetCode 3477 - Fruits Into Baskets II
// https://leetcode.com/problems/fruits-into-baskets-ii/

object Solution {
  def numOfUnplacedFruits(fruits: Array[Int], baskets: Array[Int]): Int = {
    val used = new Array[Boolean](baskets.length)
    var unplaced = 0
    fruits.foreach { f =>
      var placed = false
      var j = 0
      while (j < baskets.length && !placed) {
        if (!used(j) && baskets(j) >= f) {
          used(j) = true
          placed = true
        }
        j += 1
      }
      if (!placed) unplaced += 1
    }
    unplaced
  }
}
