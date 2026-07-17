// LeetCode 1708 - Largest Subarray Length K
// https://leetcode.com/problems/largest-subarray-length-k/

object Solution {
  def largestSubarray(nums: Array[Int], k: Int): Array[Int] = {
    var start = 0
    for (i <- 1 to nums.length - k) {
      if (nums(i) > nums(start)) {
        start = i
      }
    }
    nums.slice(start, start + k)
  }
}
