// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

object Solution {
  def transformArray(nums: Array[Int]): Array[Int] = {
    var i = 0
    while (i < nums.length) {
      nums(i) %= 2
      i += 1
    }
    var j = 0
    i = 0
    while (i < nums.length) {
      if (nums(i) == 0) {
        val t = nums(i); nums(i) = nums(j); nums(j) = t
        j += 1
      }
      i += 1
    }
    nums
  }
}
