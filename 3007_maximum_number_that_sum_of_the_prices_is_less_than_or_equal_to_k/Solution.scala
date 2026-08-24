// LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

object Solution {
  def findMaximumNumber(k: Long, x: Int): Long = {
    var num = 0L
    var f = Array.ofDim[Long](65, 65)
    def dfs(pos: Int, cnt: Int, limit: Boolean): Long = {
      if (pos == 0) return cnt
      if (!limit && f(pos)(cnt) != -1) return f(pos)(cnt)
      var ans = 0L
      val up = if (limit) ((num >> (pos - 1)) & 1).toInt else 1
      var i = 0
      while (i <= up) {
        var v = cnt
        if (i == 1 && pos % x == 0) v += 1
        ans += dfs(pos - 1, v, limit && i == up)
        i += 1
      }
      if (!limit) f(pos)(cnt) = ans
      ans
    }
    var l = 1L
    var r = 100000000000000000L
    while (l < r) {
      val mid = (l + r + 1) >> 1
      num = mid
      var m = 0
      var t = num
      while (t > 0) { m += 1; t >>= 1 }
      var i = 0
      while (i < 65) {
        var j = 0
        while (j < 65) { f(i)(j) = -1; j += 1 }
        i += 1
      }
      if (dfs(m, 0, true) <= k) l = mid else r = mid - 1
    }
    l
  }
}
