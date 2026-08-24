// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

object Solution {
  def maximumLength(s: String): Int = {
    val n = s.length
    var ans = -1
    var i = 0
    while (i < n) {
      var j = i
      var stop = false
      while (j < n && !stop) {
        if (s.charAt(j) != s.charAt(i)) stop = true
        else {
          val len = j - i + 1
          var cnt = 0
          var k = 0
          while (k + len <= n) {
            var ok = true
            var t = 0
            while (t < len && ok) {
              if (s.charAt(k + t) != s.charAt(i + t)) ok = false
              t += 1
            }
            if (ok) cnt += 1
            k += 1
          }
          if (cnt >= 3 && len > ans) ans = len
          j += 1
        }
      }
      i += 1
    }
    ans
  }
}
