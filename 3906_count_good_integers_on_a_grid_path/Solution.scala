// LeetCode 3906 - Count Good Integers On A Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

object Solution {
  private val key = new Array[Boolean](16)
  private var s = ""
  private val f = Array.ofDim[Long](16, 10)

  def countGoodIntegersOnPath(l: Long, r: Long, directions: String): Long = {
    java.util.Arrays.fill(key, false)
    var row = 0
    var col = 0
    key(0) = true
    directions.foreach { c =>
      if (c == 'D') row += 1
      else col += 1
      key(row * 4 + col) = true
    }
    calc(r) - calc(l - 1)
  }

  private def dfs(pos: Int, last: Int, lim: Boolean): Long = {
    if (pos == 16) return 1
    if (!lim && f(pos)(last) != -1) return f(pos)(last)
    var res = 0L
    val start = if (key(pos)) last else 0
    val end = if (lim) s.charAt(pos) - '0' else 9
    var i = start
    while (i <= end) {
      val nextLast = if (key(pos)) i else last
      res += dfs(pos + 1, nextLast, lim && (i == end))
      i += 1
    }
    if (!lim) f(pos)(last) = res
    res
  }

  private def calc(x: Long): Long = {
    if (x < 0) return 0
    val t = x.toString
    s = "0" * (16 - t.length) + t
    var i = 0
    while (i < 16) {
      java.util.Arrays.fill(f(i), -1L)
      i += 1
    }
    dfs(0, 0, true)
  }
}
