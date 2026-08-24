// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

object Solution {
  def maximumBobPoints(numArrows: Int, aliceArrows: Array[Int]): Array[Int] = {
    var bestScore = -1
    var best = Array.fill(12)(0)
    def dfs(i: Int, remain: Int, score: Int, bob: Array[Int]): Unit = {
      if (i == 12) {
        if (score > bestScore) {
          bestScore = score
          best = bob.clone()
          if (remain > 0) best(0) += remain
        }
        return
      }
      dfs(i + 1, remain, score, bob)
      val need = aliceArrows(i) + 1
      if (remain >= need) {
        bob(i) = need
        dfs(i + 1, remain - need, score + i, bob)
        bob(i) = 0
      }
    }
    dfs(0, numArrows, 0, Array.fill(12)(0))
    best
  }
}
