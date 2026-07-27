// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

object Solution {
  def bestCoordinate(towers: Array[Array[Int]], radius: Int): Array[Int] = {
    var best = Array(0, 0)
    var quality = -1
    for (x <- 0 to 50; y <- 0 to 50) {
      var q = 0
      for (t <- towers) {
        val d = math.hypot(x - t(0), y - t(1))
        if (d <= radius) q += (t(2) / (1 + d)).toInt
      }
      if (q > quality) {
        quality = q
        best = Array(x, y)
      }
    }
    best
  }
}
