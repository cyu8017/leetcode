// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

object Solution {
  def minOperations(s1: String, s2: String): Int = {
    val infinity = 1000000000
    var dp = Array(0, infinity)
    val n = s1.length
    var i = 0
    while (i < n) {
      val next = Array(infinity, infinity)
      var forcedZero = 0
      while (forcedZero <= 1) {
        if (dp(forcedZero) != infinity) {
          var current = s1.charAt(i)
          if (forcedZero == 1) current = '0'
          var direct = dp(forcedZero)
          if (current == '0' && s2.charAt(i) == '1') direct += 1
          else if (current == '1' && s2.charAt(i) == '0') direct = infinity
          next(0) = math.min(next(0), direct)
          if (i + 1 < n) {
            var cost = dp(forcedZero) + 1
            if (current == '0') cost += 1
            if (s1.charAt(i + 1) == '0') cost += 1
            if (s2.charAt(i) == '1') cost += 1
            next(1) = math.min(next(1), cost)
          }
        }
        forcedZero += 1
      }
      dp = next
      i += 1
    }
    if (dp(0) == infinity) -1 else dp(0)
  }
}
