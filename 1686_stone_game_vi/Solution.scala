// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

object Solution {
  def stoneGameVI(aliceValues: Array[Int], bobValues: Array[Int]): Int = {
    val n = aliceValues.length
    val order = (0 until n).sortBy(i => -(aliceValues(i) + bobValues(i)))
    var score = 0
    for ((i, t) <- order.zipWithIndex) {
      if (t % 2 == 0) score += aliceValues(i)
      else score -= bobValues(i)
    }
    if (score > 0) 1 else if (score < 0) -1 else 0
  }
}
