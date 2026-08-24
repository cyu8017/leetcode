// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

object Solution {
  def last(nums: Array[Int]): Int = {
    if (nums == null || nums.isEmpty) -1
    else nums(nums.length - 1)
  }
}
