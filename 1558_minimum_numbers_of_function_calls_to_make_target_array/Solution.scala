// LeetCode 1558 - Minimum Numbers of Function Calls to Make Target Array
// https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val adds = nums.map(Integer.bitCount).sum
    val shifts = if (nums.isEmpty) 0 else nums.map(x => if (x == 0) 0 else 31 - Integer.numberOfLeadingZeros(x)).max
    adds + shifts
  }
}
