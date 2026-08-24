// LeetCode 0664 - Strange Printer
// https://leetcode.com/problems/strange-printer/

object Solution {
  def strangePrinter(s: String): Int = {
    val n = s.length
    if (n == 0) return 0
    val dp = Array.ofDim[Int](n, n)
    var i = n - 1
    while (i >= 0) {
      dp(i)(i) = 1
      var j = i + 1
      while (j < n) {
        dp(i)(j) = dp(i + 1)(j) + 1
        var k = i + 1
        while (k <= j) {
          if (s.charAt(k) == s.charAt(i)) {
            dp(i)(j) = math.min(dp(i)(j), dp(i)(k - 1) + (if (k + 1 <= j) dp(k + 1)(j) else 0))
          }
          k += 1
        }
        j += 1
      }
      i -= 1
    }
    dp(0)(n - 1)
  }
}
