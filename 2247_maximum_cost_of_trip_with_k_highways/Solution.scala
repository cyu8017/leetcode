// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

object Solution {
  def maximumCost(n: Int, highways: Array[Array[Int]], k: Int): Int = {
    if (k + 1 > n) return -1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    for (h <- highways) {
      g(h(0)) += ((h(1), h(2)))
      g(h(1)) += ((h(0), h(2)))
    }
    val dp = Array.fill(1 << n, n)(-1)
    var i = 0
    while (i < n) {
      dp(1 << i)(i) = 0
      i += 1
    }
    var ans = -1
    var mask = 0
    while (mask < (1 << n)) {
      val cities = Integer.bitCount(mask)
      var u = 0
      while (u < n) {
        if (dp(mask)(u) >= 0) {
          if (cities - 1 == k) ans = math.max(ans, dp(mask)(u))
          for ((v, w) <- g(u) if (mask & (1 << v)) == 0) {
            val nm = mask | (1 << v)
            dp(nm)(v) = math.max(dp(nm)(v), dp(mask)(u) + w)
          }
        }
        u += 1
      }
      mask += 1
    }
    ans
  }
}
