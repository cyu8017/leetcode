// LeetCode 3399 - Smallest Substring With Identical Characters II
// https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

object Solution {
  def minLength(s: String, numOps: Int): Int = {
    val n = s.length
    var lo = 1
    var hi = n
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(s, n, numOps, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(s: String, n: Int, numOps: Int, L: Int): Boolean = {
    var ops = 0
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      ops += (j - i) / (L + 1)
      i = j
    }
    ops <= numOps
  }
}
