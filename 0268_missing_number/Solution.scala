// LeetCode 0268 - Missing Number
// https://leetcode.com/problems/missing-number/

object Solution {
  def missingNumber(nums: Array[Int]): Int = {
    val length = nums.length
    val expected = length * (length + 1) / 2
    expected - nums.sum
  }
}
