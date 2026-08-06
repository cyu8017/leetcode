// LeetCode 1515 - Best Position for a Service Centre
// https://leetcode.com/problems/best-position-for-a-service-centre/

object Solution {
  def getMinDistSum(positions: Array[Array[Int]]): Double = {
    var x = positions.map(_(0).toDouble).sum / positions.length
    var y = positions.map(_(1).toDouble).sum / positions.length
    def dist(a: Double, b: Double): Double =
      positions.map(p => math.hypot(a - p(0), b - p(1))).sum
    var iter = 0
    while (iter < 10000) {
      var nxSum = 0.0
      var nySum = 0.0
      var den = 0.0
      var coincident: Option[(Double, Double)] = None
      for (p <- positions if coincident.isEmpty) {
        val d = math.hypot(x - p(0), y - p(1))
        if (d < 1e-12) coincident = Some((p(0).toDouble, p(1).toDouble))
        else {
          nxSum += p(0) / d
          nySum += p(1) / d
          den += 1.0 / d
        }
      }
      val (nx, ny) = coincident.getOrElse((nxSum / den, nySum / den))
      if (math.hypot(nx - x, ny - y) < 1e-8) {
        x = nx; y = ny
        iter = 10000
      } else {
        x = nx; y = ny
        iter += 1
      }
    }
    dist(x, y)
  }
}
