// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

object Solution {
  def minDominoRotations(tops: Array[Int], bottoms: Array[Int]): Int = {
    def check(target: Int): Int = {
      var rotTop = 0
      var rotBot = 0
      for (i <- tops.indices) {
        if (tops(i) != target && bottoms(i) != target) return Int.MaxValue
        if (tops(i) != target) rotTop += 1
        if (bottoms(i) != target) rotBot += 1
      }
      math.min(rotTop, rotBot)
    }
    val ans = math.min(check(tops(0)), check(bottoms(0)))
    if (ans == Int.MaxValue) -1 else ans
  }
}
