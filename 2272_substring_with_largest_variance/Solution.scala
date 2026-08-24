// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

object Solution {
  def largestVariance(s: String): Int = {
    var ans = 0
    var a = 'a'
    while (a <= 'z') {
      var b = 'a'
      while (b <= 'z') {
        if (a != b) {
          var bal = 0
          var hasB = false
          var i = 0
          while (i < s.length) {
            val c = s.charAt(i)
            if (c == a) bal += 1
            else if (c == b) {
              bal -= 1
              hasB = true
            }
            if (hasB) ans = math.max(ans, bal)
            if (bal < 0) {
              bal = 0
              hasB = false
            }
            i += 1
          }
        }
        b = (b + 1).toChar
      }
      a = (a + 1).toChar
    }
    ans
  }
}
