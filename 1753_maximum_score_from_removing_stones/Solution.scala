// LeetCode 1753 - Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones/

object Solution {
  def maximumScore(a: Int, b: Int, c: Int): Int = {
    var stones = Array(a, b, c).sorted(Ordering.Int.reverse)
    var score = 0
    while (stones(0) > 0 && stones(1) > 0) {
      stones(0) -= 1
      stones(1) -= 1
      score += 1
      stones = stones.sorted(Ordering.Int.reverse)
    }
    score
  }
}
