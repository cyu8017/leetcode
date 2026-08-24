// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

object Solution {
  def minimumOperations(nums: Array[Int]): Int = {
    var ops = 0
    var i = nums.length - 2
    while (i >= 0) {
      if (nums(i) != nums(i + 1)) ops += 1
      i -= 1
    }
    ops
  }
}
