// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

object Solution {
  def longestSubarray(nums: Array[Int]): Int = {
    var mx = nums(0)
    var i = 1
    while (i < nums.length) {
      if (nums(i) > mx) mx = nums(i)
      i += 1
    }
    var ans = 0
    var cur = 0
    i = 0
    while (i < nums.length) {
      if (nums(i) == mx) {
        cur += 1
        if (cur > ans) ans = cur
      } else {
        cur = 0
      }
      i += 1
    }
    ans
  }
}
