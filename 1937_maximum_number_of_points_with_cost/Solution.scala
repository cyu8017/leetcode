// LeetCode 1937 - Maximum Number of Points with Cost
// https://leetcode.com/problems/maximum-number-of-points-with-cost/

object Solution {
  def maxPoints(points: Array[Array[Int]]): Long = {
    val m = points.length
    val n = points(0).length
    var dp = points(0).map(_.toLong)
    for (r <- 1 until m) {
      val left = Array.ofDim[Long](n)
      val right = Array.ofDim[Long](n)
      left(0) = dp(0)
      for (c <- 1 until n) left(c) = math.max(left(c - 1) - 1, dp(c))
      right(n - 1) = dp(n - 1)
      for (c <- n - 2 to 0 by -1) right(c) = math.max(right(c + 1) - 1, dp(c))
      dp = Array.tabulate(n)(c => points(r)(c) + math.max(left(c), right(c)))
    }
    dp.max
  }
}
