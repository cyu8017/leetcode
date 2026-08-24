// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

object Solution {
  def hasTrailingZeros(nums: Array[Int]): Boolean = {
    var even = 0
    for (v <- nums) {
      if (v % 2 == 0) {
        even += 1
        if (even >= 2) return true
      }
    }
    false
  }
}
