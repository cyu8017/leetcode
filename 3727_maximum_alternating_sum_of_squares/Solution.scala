// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

object Solution {
  def maxAlternatingSum(nums: Array[Int]): Long = {
    var i = 0
    while (i < nums.length) {
      nums(i) *= nums(i)
      i += 1
    }
    java.util.Arrays.sort(nums)
    val m = nums.length / 2
    var ans = 0L
    i = 0
    while (i < m) {
      ans -= nums(i)
      i += 1
    }
    i = m
    while (i < nums.length) {
      ans += nums(i)
      i += 1
    }
    ans
  }
}
