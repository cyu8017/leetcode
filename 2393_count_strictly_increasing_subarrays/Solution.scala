// LeetCode 2393 - Count Strictly Increasing Subarrays
// https://leetcode.com/problems/count-strictly-increasing-subarrays/

object Solution {
  def countSubarrays(nums: Array[Int]): Long = {
    var ans = 0L
    var len = 0L
    var i = 0
    while (i < nums.length) {
      if (i > 0 && nums(i) > nums(i - 1)) len += 1
      else len = 1
      ans += len
      i += 1
    }
    ans
  }
}
