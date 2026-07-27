// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

object Solution {
  def getSumAbsoluteDifferences(nums: Array[Int]): Array[Int] = {
    val total = nums.sum
    val n = nums.length
    val ans = Array.fill(n)(0)
    var left = 0
    for (i <- nums.indices) {
      val x = nums(i)
      ans(i) = x * i - left + (total - left - x) - x * (n - i - 1)
      left += x
    }
    ans
  }
}
