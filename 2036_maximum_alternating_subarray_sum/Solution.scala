// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

object Solution {
  def maximumAlternatingSubarraySum(nums: Array[Int]): Long = {
    var ans = Long.MinValue
    var even = 0L
    var i = 0
    while (i < nums.length) {
      val x = nums(i).toLong
      if (i % 2 == 0) even += x
      else even = math.max(0L, even - x)
      ans = math.max(ans, even)
      i += 1
    }
    var odd = 0L
    i = 1
    while (i < nums.length) {
      val x = nums(i).toLong
      if (i % 2 == 1) odd += x
      else odd = math.max(0L, odd - x)
      ans = math.max(ans, odd)
      i += 1
    }
    ans
  }
}
