// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/

object Solution {
  def countValidPrefixes(s: String): Int = {
    var ans = 0
    var t = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '1') t += 1
      else t -= 1
      if (t >= -1 && t <= 1) ans += 1
      i += 1
    }
    ans
  }
}
