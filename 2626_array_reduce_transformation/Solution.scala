// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

object Solution {
  def reduce(nums: Array[Int], fn: (Int, Int) => Int, init: Int): Int = {
    var acc = init
    var i = 0
    while (i < nums.length) {
      acc = fn(acc, nums(i))
      i += 1
    }
    acc
  }
}
