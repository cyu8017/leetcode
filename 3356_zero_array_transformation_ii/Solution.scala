// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

object Solution {
  def minZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val n = nums.length
    if (ok(0, nums, queries, n)) return 0
    var lo = 1
    var hi = queries.length + 1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (mid <= queries.length && ok(mid, nums, queries, n)) hi = mid
      else lo = mid + 1
    }
    if (lo > queries.length) -1 else lo
  }

  private def ok(k: Int, nums: Array[Int], queries: Array[Array[Int]], n: Int): Boolean = {
    val diff = new Array[Long](n + 1)
    var i = 0
    while (i < k) {
      val q = queries(i)
      diff(q(0)) += q(2)
      diff(q(1) + 1) -= q(2)
      i += 1
    }
    var cur = 0L
    i = 0
    while (i < n) {
      cur += diff(i)
      if (cur < nums(i)) return false
      i += 1
    }
    true
  }
}
