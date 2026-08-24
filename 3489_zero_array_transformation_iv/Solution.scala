// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

object Solution {
  private def canSubsetSum(vals: java.util.List[Integer], target: Int): Boolean = {
    if (target == 0) return true
    val dp = new Array[Boolean](target + 1)
    dp(0) = true
    val it = vals.iterator()
    while (it.hasNext) {
      val v = it.next().intValue()
      var s = target
      while (s >= v) {
        if (dp(s - v)) dp(s) = true
        s -= 1
      }
    }
    dp(target)
  }

  def minZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    if (ok(nums, queries, 0)) return 0
    var lo = 1
    var hi = queries.length + 1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (mid <= queries.length && ok(nums, queries, mid)) hi = mid
      else lo = mid + 1
    }
    if (lo > queries.length) -1 else lo
  }

  private def ok(nums: Array[Int], queries: Array[Array[Int]], k: Int): Boolean = {
    val n = nums.length
    var i = 0
    while (i < n) {
      if (nums(i) != 0) {
        val vals = new java.util.ArrayList[Integer]()
        var q = 0
        while (q < k) {
          val l = queries(q)(0)
          val r = queries(q)(1)
          val v = queries(q)(2)
          if (l <= i && i <= r) vals.add(v)
          q += 1
        }
        if (!canSubsetSum(vals, nums(i))) return false
      }
      i += 1
    }
    true
  }
}
