// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

object Solution {
  def countSubstrings(s: String): Long = {
    var ans = 0L
    val n = s.length
    var r = 0
    while (r < n) {
      val last = s.charAt(r) - '0'
      if (last != 0) {
        var mod = 0
        var p = 1 % last
        var l = r
        while (l >= 0) {
          mod = (mod + (s.charAt(l) - '0') * p) % last
          p = (p * 10) % last
          if (mod == 0) ans += 1
          l -= 1
        }
      }
      r += 1
    }
    ans
  }
}
