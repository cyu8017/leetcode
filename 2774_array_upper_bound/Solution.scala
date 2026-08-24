// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

object Solution {
  def upperBound(nums: Array[Int], target: Int): Int = {
    var lo = 0
    var hi = nums.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (nums(mid) <= target) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
