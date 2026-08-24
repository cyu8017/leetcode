// LeetCode 3674 - Minimum Operations to Equalize Array
// https://leetcode.com/problems/minimum-operations-to-equalize-array/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    for (x <- nums) if (x != nums(0)) return 1
    0
  }
}
