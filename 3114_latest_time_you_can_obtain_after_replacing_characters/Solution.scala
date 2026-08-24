// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

object Solution {
  def findLatestTime(s: String): String = {
    var h = 11
    while (true) {
      var m = 59
      while (m >= 0) {
        val t = "%02d:%02d".format(h, m)
        var ok = true
        var i = 0
        while (i < 5 && ok) {
          if (s.charAt(i) != '?' && s.charAt(i) != t.charAt(i)) ok = false
          i += 1
        }
        if (ok) return t
        m -= 1
      }
      h -= 1
    }
    ""
  }
}
