// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

object Solution {
  def minimizeMax(nums: Array[Int], p: Int): Int = {
    java.util.Arrays.sort(nums)
    var lo = 0
    var hi = nums(nums.length - 1) - nums(0)
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(nums, p, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(nums: Array[Int], p: Int, d: Int): Boolean = {
    var cnt = 0
    var i = 0
    while (i + 1 < nums.length) {
      if (nums(i + 1) - nums(i) <= d) {
        cnt += 1
        i += 2
      } else i += 1
    }
    cnt >= p
  }
}
