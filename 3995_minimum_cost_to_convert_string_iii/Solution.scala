// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

object Solution {
  def minCost(source: String, target: String, rules: Array[Array[String]], costs: Array[Int]): Int = {
    val n = source.length
    if (target.length != n) return -1
    val dp = Array.fill(n + 1)(Int.MaxValue)
    dp(0) = 0
    var i = 0
    while (i < n) {
      if (dp(i) != Int.MaxValue) {
        if (source.charAt(i) == target.charAt(i) && dp(i) < dp(i + 1)) dp(i + 1) = dp(i)
        var j = 0
        while (j < rules.length) {
          val p = rules(j)(0)
          val r = rules(j)(1)
          val plen = p.length
          if (i + plen <= n) {
            var c = costs(j)
            var ok = true
            var k = 0
            while (k < plen && ok) {
              if (r.charAt(k) != target.charAt(i + k)) ok = false
              else if (p.charAt(k) == '*') c += 1
              else if (p.charAt(k) != source.charAt(i + k)) ok = false
              k += 1
            }
            if (ok && dp(i) <= Int.MaxValue - c && dp(i) + c < dp(i + plen)) {
              dp(i + plen) = dp(i) + c
            }
          }
          j += 1
        }
      }
      i += 1
    }
    if (dp(n) == Int.MaxValue) -1 else dp(n)
  }
}
