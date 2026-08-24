// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

object Solution {
  def longestSubarray(nums: Array[Int]): Int = {
    var f = 2
    var ans = f
    var i = 2
    while (i < nums.length) {
      if (nums(i) == nums(i - 1) + nums(i - 2)) {
        f += 1
        ans = math.max(ans, f)
      } else f = 2
      i += 1
    }
    ans
  }
}
