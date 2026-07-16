// LeetCode 0136 - Single Number
// https://leetcode.com/problems/single-number/

object Solution {
  def singleNumber(nums: Array[Int]): Int = nums.foldLeft(0)(_ ^ _)
}
