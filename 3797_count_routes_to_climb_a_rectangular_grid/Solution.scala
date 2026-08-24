// LeetCode 3797 - Count Routes To Climb A Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

object Solution {
  def countRoutes(grid: Array[String], d: Int): Int = {
    val MOD = 1000000007
    val n = grid.length
    val m = grid(0).length
    var upRadius = 0
    while ((upRadius + 1L) * (upRadius + 1) + 1 <= d.toLong * d) upRadius += 1
    var arrived = new Array[Int](m)
    var c = 0
    while (c < m) {
      if (grid(n - 1).charAt(c) == '.') arrived(c) = 1
      c += 1
    }
    var r = n - 1
    while (r >= 0) {
      val pref = new Array[Int](m + 1)
      var i = 0
      while (i < m) {
        pref(i + 1) = (pref(i) + arrived(i)) % MOD
        i += 1
      }
      val horizontal = new Array[Int](m)
      c = 0
      while (c < m) {
        if (grid(r).charAt(c) != '#') {
          val l = math.max(0, c - d)
          val rr = math.min(m - 1, c + d)
          horizontal(c) = (pref(rr + 1) - pref(l) - arrived(c)) % MOD
          if (horizontal(c) < 0) horizontal(c) += MOD
        }
        c += 1
      }
      if (r == 0) {
        var ans = 0
        c = 0
        while (c < m) {
          ans = (ans + arrived(c) + horizontal(c)) % MOD
          c += 1
        }
        return ans
      }
      val pref2 = new Array[Int](m + 1)
      c = 0
      while (c < m) {
        pref2(c + 1) = (pref2(c) + arrived(c) + horizontal(c)) % MOD
        c += 1
      }
      val next = new Array[Int](m)
      c = 0
      while (c < m) {
        if (grid(r - 1).charAt(c) != '#') {
          val l = math.max(0, c - upRadius)
          val rr = math.min(m - 1, c + upRadius)
          next(c) = pref2(rr + 1) - pref2(l)
          if (next(c) < 0) next(c) += MOD
        }
        c += 1
      }
      arrived = next
      r -= 1
    }
    0
  }
}
