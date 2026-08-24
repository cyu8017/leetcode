// LeetCode 2312 - Selling Pieces of Wood
// https://leetcode.com/problems/selling-pieces-of-wood/

object Solution {
  def sellingWood(m: Int, n: Int, prices: Array[Array[Int]]): Long = {
    val price = Array.ofDim[Long](m + 1, n + 1)
    val dp = Array.ofDim[Long](m + 1, n + 1)
    prices.foreach { p => price(p(0))(p(1)) = p(2) }
    var h = 1
    while (h <= m) {
      var w = 1
      while (w <= n) {
        var best = price(h)(w)
        var i = 1
        while (i < h) {
          best = math.max(best, dp(i)(w) + dp(h - i)(w))
          i += 1
        }
        var j = 1
        while (j < w) {
          best = math.max(best, dp(h)(j) + dp(h)(w - j))
          j += 1
        }
        dp(h)(w) = best
        w += 1
      }
      h += 1
    }
    dp(m)(n)
  }
}
