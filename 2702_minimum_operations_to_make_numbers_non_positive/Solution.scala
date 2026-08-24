// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

object Solution {
  def minOperations(nums: Array[Int], x: Int, y: Int): Int = {
    var lo = 0
    var hi = 0
    var i = 0
    while (i < nums.length) {
      val v = nums(i)
      hi = math.max(hi, (v + y - 1) / y)
      hi = math.max(hi, (v + x - 1) / x)
      i += 1
    }
    hi += nums.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(nums, x, y, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(nums: Array[Int], x: Int, y: Int, ops: Int): Boolean = {
    var extra = 0L
    var i = 0
    while (i < nums.length) {
      val remain = nums(i).toLong - ops.toLong * y
      if (remain > 0) extra += (remain + (x - y) - 1) / (x - y)
      i += 1
    }
    extra <= ops
  }
}
