// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

object Solution {
  def stoneGameVIII(stones: Array[Int]): Int = {
    val n = stones.length
    for (i <- 1 until n) {
      stones(i) += stones(i - 1)
    }
    var score = stones(n - 1)
    for (i <- n - 2 to 1 by -1) {
      score = math.max(stones(i) - score, score)
    }
    score
  }
}
