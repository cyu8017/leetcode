// LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

object Solution {
  def countKConstraintSubstrings(s: String, k: Int, queries: Array[Array[Int]]): Array[Long] = {
    val n = s.length
    val leftMost = new Array[Int](n)
    var z = 0
    var o = 0
    var L = 0
    var R = 0
    while (R < n) {
      if (s.charAt(R) == '0') z += 1 else o += 1
      while (z > k && o > k) {
        if (s.charAt(L) == '0') z -= 1 else o -= 1
        L += 1
      }
      leftMost(R) = L
      R += 1
    }
    val pref = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + (i - leftMost(i) + 1)
      i += 1
    }
    val ans = new Array[Long](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val l = queries(qi)(0)
      val r = queries(qi)(1)
      var lo = l
      var hi = r + 1
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (leftMost(mid) < l) lo = mid + 1 else hi = mid
      }
      var res = 0L
      if (lo > l) {
        val m = (lo - l).toLong
        res += m * (m + 1) / 2
      }
      if (lo <= r) res += pref(r + 1) - pref(lo)
      ans(qi) = res
      qi += 1
    }
    ans
  }
}
