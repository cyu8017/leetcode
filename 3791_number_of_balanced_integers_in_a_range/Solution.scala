// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

object Solution {
  private val BASE = 90

  def countBalanced(low0: Long, high: Long): Long = {
    if (high < 11) return 0
    var low = low0
    if (low < 11) low = 11
    var num = ""
    val f = Array.fill(20, 181)(-1L)

    def dfs(pos: Int, diff: Int, lim: Boolean): Long = {
      if (pos >= num.length) return if (diff == 0) 1 else 0
      if (!lim && f(pos)(diff + BASE) != -1) return f(pos)(diff + BASE)
      val up = if (lim) num.charAt(pos) - '0' else 9
      var res = 0L
      var i = 0
      while (i <= up) {
        if (pos % 2 == 0) res += dfs(pos + 1, diff + i, lim && i == up)
        else res += dfs(pos + 1, diff - i, lim && i == up)
        i += 1
      }
      if (!lim) f(pos)(diff + BASE) = res
      res
    }

    num = java.lang.Long.toString(low - 1)
    var r = 0
    while (r < 20) {
      java.util.Arrays.fill(f(r), -1L)
      r += 1
    }
    val a = dfs(0, 0, lim = true)
    num = java.lang.Long.toString(high)
    r = 0
    while (r < 20) {
      java.util.Arrays.fill(f(r), -1L)
      r += 1
    }
    val b = dfs(0, 0, lim = true)
    b - a
  }
}
