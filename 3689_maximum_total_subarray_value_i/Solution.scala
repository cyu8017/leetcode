// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

object Solution {
  def maxTotalValue(nums: Array[Int], k: Int): Long = {
    var mn = nums(0)
    var mx = nums(0)
    for (x <- nums) {
      mn = math.min(mn, x)
      mx = math.max(mx, x)
    }
    1L * k * (mx - mn)
  }
}
