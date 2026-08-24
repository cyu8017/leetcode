// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

object Solution {
  def numberOfWays(s: String): Long = {
    var total0 = 0
    var total1 = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '0') total0 += 1 else total1 += 1
      i += 1
    }
    var left0 = 0
    var left1 = 0
    var ans = 0L
    i = 0
    while (i < s.length) {
      if (s.charAt(i) == '0') {
        ans += left1.toLong * (total1 - left1)
        left0 += 1
      } else {
        ans += left0.toLong * (total0 - left0)
        left1 += 1
      }
      i += 1
    }
    ans
  }
}
