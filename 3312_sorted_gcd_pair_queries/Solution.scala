// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

object Solution {
  def gcdValues(nums: Array[Int], queries: Array[Long]): Array[Int] = {
    var maxV = 0
    for (x <- nums) if (x > maxV) maxV = x
    val cnt = new Array[Int](maxV + 1)
    for (x <- nums) cnt(x) += 1
    val divCnt = new Array[Long](maxV + 1)
    var g = 1
    while (g <= maxV) {
      var c = 0L
      var m = g
      while (m <= maxV) {
        c += cnt(m)
        m += g
      }
      divCnt(g) = c * (c - 1) / 2
      g += 1
    }
    val exact = new Array[Long](maxV + 1)
    g = maxV
    while (g >= 1) {
      exact(g) = divCnt(g)
      var m = 2 * g
      while (m <= maxV) {
        exact(g) -= exact(m)
        m += g
      }
      g -= 1
    }
    val pref = new Array[Long](maxV + 1)
    g = 1
    while (g <= maxV) {
      pref(g) = pref(g - 1) + exact(g)
      g += 1
    }
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      val q = queries(i)
      var lo = 1
      var hi = maxV
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (pref(mid) > q) hi = mid
        else lo = mid + 1
      }
      ans(i) = lo
      i += 1
    }
    ans
  }
}
