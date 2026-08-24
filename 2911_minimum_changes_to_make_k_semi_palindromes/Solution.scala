// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

object Solution {
  private var s: String = _

  def minimumChanges(s: String, k: Int): Int = {
    this.s = s
    val n = s.length
    val cost = Array.fill(n, n)(1 << 20)
    for (i <- 0 until n; j <- i + 1 until n) cost(i)(j) = semiCost(i, j)
    val dp = Array.fill(k + 1, n + 1)(1 << 20)
    dp(0)(0) = 0
    for (p <- 1 to k; i <- 1 to n; t <- 0 until i - 1) {
      val cand = dp(p - 1)(t) + cost(t)(i - 1)
      if (cand < dp(p)(i)) dp(p)(i) = cand
    }
    dp(k)(n)
  }

  private def semiCost(l: Int, r: Int): Int = {
    val length = r - l + 1
    var best = 1 << 20
    for (d <- 1 until length if length % d == 0) {
      var chg = 0
      for (start <- 0 until d) {
        val chars = new StringBuilder
        var i = l + start
        while (i <= r) {
          chars.append(s.charAt(i))
          i += d
        }
        var a = 0
        var b = chars.length - 1
        while (a < b) {
          if (chars.charAt(a) != chars.charAt(b)) chg += 1
          a += 1
          b -= 1
        }
      }
      if (chg < best) best = chg
    }
    best
  }
}
