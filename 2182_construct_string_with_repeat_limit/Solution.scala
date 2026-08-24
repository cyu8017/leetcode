// LeetCode 2182 - Construct String With Repeat Limit
// https://leetcode.com/problems/construct-string-with-repeat-limit/

object Solution {
  def repeatLimitedString(s: String, repeatLimit: Int): String = {
    val freq = Array.fill(26)(0)
    var i = 0
    while (i < s.length) {
      freq(s.charAt(i) - 'a') += 1
      i += 1
    }
    val ans = new StringBuilder
    var placed = true
    while (placed) {
      placed = false
      var c = 25
      var done = false
      while (c >= 0 && !done) {
        if (freq(c) != 0) {
          if (ans.length > 0 && ans.charAt(ans.length - 1) - 'a' == c) {
            var found = false
            var d = c - 1
            while (d >= 0 && !found) {
              if (freq(d) > 0) {
                ans.append(('a' + d).toChar)
                freq(d) -= 1
                found = true
                placed = true
              }
              d -= 1
            }
            if (!found) return ans.toString
            done = true
          } else {
            val use = math.min(freq(c), repeatLimit)
            i = 0
            while (i < use) {
              ans.append(('a' + c).toChar)
              i += 1
            }
            freq(c) -= use
            placed = true
            done = true
          }
        }
        c -= 1
      }
    }
    ans.toString
  }
}
