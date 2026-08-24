// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

object Solution {
  def hasIncreasingSubarrays(nums: Array[Int], k: Int): Boolean = {
    val n = nums.length
    var i = 0
    while (i + 2 * k <= n) {
      if (inc(nums, i, k) && inc(nums, i + k, k)) return true
      i += 1
    }
    false
  }

  private def inc(nums: Array[Int], start: Int, k: Int): Boolean = {
    var i = start
    while (i + 1 < start + k) {
      if (nums(i) >= nums(i + 1)) return false
      i += 1
    }
    true
  }
}
