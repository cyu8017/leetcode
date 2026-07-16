// LeetCode 0091 - Decode Ways
// https://leetcode.com/problems/decode-ways/

object Solution {
  def numDecodings(s: String): Int = {
    if (s == null || s.isEmpty || s.charAt(0) == '0') {
      return 0
    }

    var prev2 = 1
    var prev1 = 1

    var i = 1
    while (i < s.length) {
      var current = 0
      if (s.charAt(i) != '0') {
        current += prev1
      }
      val two = s.substring(i - 1, i + 1).toInt
      if (two >= 10 && two <= 26) {
        current += prev2
      }
      prev2 = prev1
      prev1 = current
      i += 1
    }

    prev1
  }
}
