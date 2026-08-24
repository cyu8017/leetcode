// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

object Solution {
  def minimumTotalDistance(robot: List[Int], factory: Array[Array[Int]]): Long = {
    val robots = robot.sorted
    val fac = factory.sortBy(_(0))
    val m = robots.length
    val pos = scala.collection.mutable.ArrayBuffer.empty[Int]
    fac.foreach { f =>
      var c = 0
      while (c < f(1)) {
        pos += f(0)
        c += 1
      }
    }
    val n = pos.length
    val INF = 1L << 60
    val dp = Array.fill(m + 1, n + 1)(INF)
    var j = 0
    while (j <= n) {
      dp(0)(j) = 0
      j += 1
    }
    var i = 1
    while (i <= m) {
      j = i
      while (j <= n) {
        dp(i)(j) = dp(i)(j - 1)
        var diff = robots(i - 1).toLong - pos(j - 1)
        if (diff < 0) diff = -diff
        if (dp(i - 1)(j - 1) + diff < dp(i)(j)) dp(i)(j) = dp(i - 1)(j - 1) + diff
        j += 1
      }
      i += 1
    }
    dp(m)(n)
  }
}
