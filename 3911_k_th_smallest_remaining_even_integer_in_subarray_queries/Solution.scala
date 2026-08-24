// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

object Solution {
  def kthSmallestEven(nums: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
    val n = nums.length
    val evenPrefix = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      evenPrefix(i + 1) = evenPrefix(i) + (if (nums(i) % 2 == 0) 1 else 0)
      i += 1
    }
    val ans = new Array[Long](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val l = queries(qi)(0)
      val r = queries(qi)(1)
      val k = queries(qi)(2).toLong
      var lo = 1L
      var hi = k + (r - l + 1)
      while (lo < hi) {
        val mid = (lo + hi) / 2
        var pos = upperBound(nums, 2 * mid)
        if (pos > r + 1) pos = r + 1
        var removed = 0
        if (pos > l) removed = evenPrefix(pos) - evenPrefix(l)
        if (mid - removed >= k) hi = mid
        else lo = mid + 1
      }
      ans(qi) = 2 * lo
      qi += 1
    }
    ans
  }

  private def upperBound(a: Array[Int], x: Long): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) <= x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
