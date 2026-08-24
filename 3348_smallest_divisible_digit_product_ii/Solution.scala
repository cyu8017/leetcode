// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

object Solution {
  private def dfs(res: Array[Char], i: Int, tight: Boolean, sameLen: Boolean, num: String, t: Long): Boolean = {
    if (i == res.length) {
      var prod = 1L
      for (c <- res) {
        prod *= (c - '0')
        if (prod == 0) return false
      }
      return prod % t == 0 && prod > 0
    }
    var start = if (i == 0) '1' else '0'
    if (tight && sameLen && i < num.length) start = num.charAt(i)
    var c = start
    while (c <= '9') {
      res(i) = c
      val nt = tight && sameLen && i < num.length && c == num.charAt(i)
      if (dfs(res, i + 1, nt, sameLen, num, t)) return true
      c = (c + 1).toChar
    }
    false
  }

  def smallestNumber(num: String, t: Long): String = {
    var tt = t
    var d = 9
    while (d >= 2) {
      while (tt % d == 0) tt /= d
      d -= 1
    }
    if (tt > 1) return "-1"
    var extra = 0
    while (extra <= 60) {
      val L = num.length + extra
      val res = new Array[Char](L)
      if (dfs(res, 0, true, extra == 0, num, t)) return new String(res)
      extra += 1
    }
    "-1"
  }
}
