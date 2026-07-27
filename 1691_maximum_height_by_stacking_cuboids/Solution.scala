// LeetCode 1691 - Maximum Height by Stacking Cuboids
// https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

object Solution {
  def maxHeight(cuboids: Array[Array[Int]]): Int = {
    val a = cuboids.map(_.sorted).sortBy(c => (c(0), c(1), c(2)))
    val n = a.length
    val dp = Array.fill(n)(0)
    var best = 0
    for (i <- 0 until n) {
      dp(i) = a(i)(2)
      for (j <- 0 until i) {
        if ((0 until 3).forall(d => a(j)(d) <= a(i)(d))) {
          dp(i) = math.max(dp(i), dp(j) + a(i)(2))
        }
      }
      best = math.max(best, dp(i))
    }
    best
  }
}
