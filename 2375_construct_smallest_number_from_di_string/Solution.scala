// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

object Solution {
  def smallestNumber(pattern: String): String = {
    val n = pattern.length
    val ans = Array.tabulate(n + 1)(i => ('1' + i).toChar)
    var i = 0
    while (i < n) {
      if (pattern.charAt(i) == 'I') i += 1
      else {
        var j = i
        while (j < n && pattern.charAt(j) == 'D') j += 1
        reverse(ans, i, j)
        i = j
      }
    }
    new String(ans)
  }

  private def reverse(a: Array[Char], l0: Int, r0: Int): Unit = {
    var l = l0
    var r = r0
    while (l < r) {
      val t = a(l)
      a(l) = a(r)
      a(r) = t
      l += 1
      r -= 1
    }
  }
}
