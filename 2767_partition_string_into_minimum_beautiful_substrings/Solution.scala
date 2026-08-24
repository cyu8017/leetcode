// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

object Solution {
  def minimumBeautifulSubstrings(s: String): Int = {
    val n = s.length
    val pow5 = scala.collection.mutable.HashSet.empty[String]
    var x = 1L
    var stop = false
    while (!stop) {
      val b = java.lang.Long.toBinaryString(x)
      if (b.length > n) stop = true
      else {
        pow5 += b
        x *= 5
      }
    }
    val INF = 1 << 30
    val dp = Array.fill(n + 1)(INF)
    dp(0) = 0
    var i = 0
    while (i < n) {
      if (dp(i) != INF && s.charAt(i) != '0') {
        var j = i + 1
        while (j <= n) {
          if (pow5.contains(s.substring(i, j))) dp(j) = math.min(dp(j), dp(i) + 1)
          j += 1
        }
      }
      i += 1
    }
    if (dp(n) == INF) -1 else dp(n)
  }
}
