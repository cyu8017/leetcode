// LeetCode 1752 - Check if Array Is Sorted and Rotated
// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

object Solution {
  def check(nums: Array[Int]): Boolean = {
    val n = nums.length
    val drops = (0 until n).count(i => nums(i) > nums((i + 1) % n))
    drops <= 1
  }
}
