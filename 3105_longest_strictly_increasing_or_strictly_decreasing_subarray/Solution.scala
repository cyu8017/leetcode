// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

object Solution {
  def longestMonotonicSubarray(nums: Array[Int]): Int = {
    var ans = 1
    var t = 1
    var i = 1
    while (i < nums.length) {
      if (nums(i - 1) < nums(i)) {
        t += 1
        ans = math.max(ans, t)
      } else t = 1
      i += 1
    }
    t = 1
    i = 1
    while (i < nums.length) {
      if (nums(i - 1) > nums(i)) {
        t += 1
        ans = math.max(ans, t)
      } else t = 1
      i += 1
    }
    ans
  }
}
