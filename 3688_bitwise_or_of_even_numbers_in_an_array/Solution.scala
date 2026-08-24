// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

object Solution {
  def evenNumberBitwiseORs(nums: Array[Int]): Int = {
    var ans = 0
    for (x <- nums) if (x % 2 == 0) ans |= x
    ans
  }
}
