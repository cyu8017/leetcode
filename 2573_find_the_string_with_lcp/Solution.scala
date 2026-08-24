// LeetCode 2573 - Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/

object Solution {
  def findTheString(lcp: Array[Array[Int]]): String = {
    val n = lcp.length
    val s = Array.fill(n)(0.toChar)
    var c = 'a'
    var i = 0
    while (i < n) {
      if (s(i) == 0) {
        if (c > 'z') return ""
        s(i) = c
        var j = i + 1
        while (j < n) {
          if (lcp(i)(j) > 0) s(j) = c
          j += 1
        }
        c = (c + 1).toChar
      }
      i += 1
    }
    i = n - 1
    while (i >= 0) {
      var j = n - 1
      while (j >= 0) {
        var v = 0
        if (s(i) == s(j)) {
          v = 1
          if (i + 1 < n && j + 1 < n) v += lcp(i + 1)(j + 1)
        }
        if (lcp(i)(j) != v) return ""
        j -= 1
      }
      i -= 1
    }
    new String(s)
  }
}
