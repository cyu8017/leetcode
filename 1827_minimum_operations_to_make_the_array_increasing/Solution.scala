// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    var ops = 0
    var prev = nums(0)
    for (i <- 1 until nums.length) {
      if (nums(i) <= prev) {
        val needed = prev + 1
        ops += needed - nums(i)
        prev = needed
      } else prev = nums(i)
    }
    ops
  }
}
