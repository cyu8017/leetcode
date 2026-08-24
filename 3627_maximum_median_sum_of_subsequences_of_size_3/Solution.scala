// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

object Solution {
  def maximumMedianSum(nums: Array[Int]): Long = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    var ans = 0L
    var i = n / 3
    while (i < n) {
      ans += nums(i)
      i += 2
    }
    ans
  }
}
