// LeetCode 3869 - Count Fancy Numbers In A Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

object Solution {
  private var num: String = _
  private var f: Array[Array[Array[Array[Long]]]] = _
  private var n: Int = _

  private def check(s: Int): Boolean = {
    if (s < 100) return s % 11 != 0
    val mid = (s / 10) % 10
    val last = s % 10
    mid > 1 && mid < last
  }

  def countFancy(l: Long, r: Long): Long = calc(r) - calc(l - 1)

  private def calc(x: Long): Long = {
    num = x.toString
    n = num.length
    f = Array.ofDim[Long](n, 9 * n + 1, 10, 4)
    var i = 0
    while (i < n) {
      var j = 0
      while (j <= 9 * n) {
        var p = 0
        while (p < 10) {
          java.util.Arrays.fill(f(i)(j)(p), -1L)
          p += 1
        }
        j += 1
      }
      i += 1
    }
    dfs(0, 0, 0, 0, true)
  }

  private def dfs(pos: Int, s: Int, prev: Int, st: Int, lim: Boolean): Long = {
    if (pos >= n) {
      if (st != 3) return 1
      return if (check(s)) 1 else 0
    }
    if (!lim && f(pos)(s)(prev)(st) != -1) return f(pos)(s)(prev)(st)
    val up = if (lim) num.charAt(pos) - '0' else 9
    var res = 0L
    var i = 0
    while (i <= up) {
      var nxtSt = st
      if (st == 0) {
        if (prev == 0) nxtSt = 0
        else if (i > prev) nxtSt = 1
        else if (i < prev) nxtSt = 2
        else nxtSt = 3
      } else if (st == 1) {
        nxtSt = if (i > prev) 1 else 3
      } else if (st == 2) {
        nxtSt = if (i < prev) 2 else 3
      } else {
        nxtSt = 3
      }
      res += dfs(pos + 1, s + i, i, nxtSt, lim && i == up)
      i += 1
    }
    if (!lim) f(pos)(s)(prev)(st) = res
    res
  }
}
