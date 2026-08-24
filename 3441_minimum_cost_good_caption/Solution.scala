// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

object Solution {
  def minCostGoodCaption(caption: String): String = {
    val n = caption.length
    if (n < 3) return ""
    val ans = caption.toCharArray
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && ans(j) == ans(i)) j += 1
      if (j - i >= 3) i = j
      else {
        val need = 3 - (j - i)
        if (j + need <= n) {
          var t = 0
          while (t < need) { ans(j + t) = ans(i); t += 1 }
          i = j + need
        } else {
          var ch = 'a'
          if (i > 0) ch = ans(i - 1)
          else if (j < n) ch = caption.charAt(j)
          var t = i
          while (t < n) { ans(t) = ch; t += 1 }
          i = n
        }
      }
    }
    i = 0
    while (i < n) {
      var j = i
      while (j < n && ans(j) == ans(i)) j += 1
      if (j - i < 3) return ""
      i = j
    }
    new String(ans)
  }
}
