// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

object Solution {
  def isZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Boolean = {
    val n = nums.length
    val diff = new Array[Int](n + 1)
    for (q <- queries) {
      diff(q(0)) += 1
      diff(q(1) + 1) -= 1
    }
    var cur = 0
    var i = 0
    while (i < n) {
      cur += diff(i)
      if (cur < nums(i)) return false
      i += 1
    }
    true
  }
}
