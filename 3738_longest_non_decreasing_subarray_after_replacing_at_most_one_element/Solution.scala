// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

object Solution {
  def longestSubarray(nums: Array[Int]): Int = {
    val n = nums.length
    val left = Array.fill(n)(1)
    val right = Array.fill(n)(1)
    var i = 1
    while (i < n) {
      if (nums(i) >= nums(i - 1)) left(i) = left(i - 1) + 1
      i += 1
    }
    i = n - 2
    while (i >= 0) {
      if (nums(i) <= nums(i + 1)) right(i) = right(i + 1) + 1
      i -= 1
    }
    var ans = 0
    left.foreach(v => ans = math.max(ans, v))
    i = 0
    while (i < n) {
      val a = if (i > 0) left(i - 1) else 0
      val b = if (i + 1 < n) right(i + 1) else 0
      if (i > 0 && i + 1 < n && nums(i - 1) > nums(i + 1)) {
        ans = math.max(ans, math.max(a + 1, b + 1))
      } else {
        ans = math.max(ans, a + b + 1)
      }
      i += 1
    }
    ans
  }
}
