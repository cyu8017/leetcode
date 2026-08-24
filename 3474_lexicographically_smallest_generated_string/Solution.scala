// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

object Solution {
  def generateString(str1: String, str2: String): String = {
    val n = str1.length
    val m = str2.length
    val L = n + m - 1
    val ans = Array.fill(L)('?')
    var i = 0
    while (i < n) {
      if (str1.charAt(i) == 'T') {
        var j = 0
        while (j < m) {
          if (ans(i + j) != '?' && ans(i + j) != str2.charAt(j)) return ""
          ans(i + j) = str2.charAt(j)
          j += 1
        }
      }
      i += 1
    }
    i = 0
    while (i < L) {
      if (ans(i) == '?') ans(i) = 'a'
      i += 1
    }
    i = 0
    while (i < n) {
      if (str1.charAt(i) == 'F') {
        var isMatch = true
        var j = 0
        while (j < m) {
          if (ans(i + j) != str2.charAt(j)) { isMatch = false; j = m }
          else j += 1
        }
        if (isMatch) {
          var changed = false
          j = m - 1
          while (j >= 0 && !changed) {
            val pos = i + j
            var forced = false
            var t = 0
            while (t < n && !forced) {
              if (str1.charAt(t) == 'T' && pos >= t && pos < t + m) forced = true
              t += 1
            }
            if (!forced) {
              ans(pos) = 'b'
              changed = true
            }
            j -= 1
          }
          if (!changed) return ""
        }
      }
      i += 1
    }
    i = 0
    while (i < n) {
      var isMatch2 = true
      var j = 0
      while (j < m) {
        if (ans(i + j) != str2.charAt(j)) { isMatch2 = false; j = m }
        else j += 1
      }
      if (str1.charAt(i) == 'T' && !isMatch2) return ""
      if (str1.charAt(i) == 'F' && isMatch2) return ""
      i += 1
    }
    new String(ans)
  }
}
