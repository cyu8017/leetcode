// LeetCode 1058 - Minimize Rounding Error to Meet Target
// https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

object Solution {
  def minimizeError(prices: Array[String], target: Int): String = {
    var floors = 0
    val fracs = scala.collection.mutable.ArrayBuffer.empty[Double]
    for (p <- prices) {
      val value = p.toDouble
      val floor = value.toInt
      floors += floor
      val frac = value - floor
      if (frac > 1e-9) fracs += frac
    }
    val ceilCount = target - floors
    if (ceilCount < 0 || ceilCount > fracs.length) return "-1"
    val sorted = fracs.sorted.reverse
    val error = sorted.take(ceilCount).map(f => 1 - f).sum + sorted.drop(ceilCount).sum
    f"$error%.3f"
  }
}
