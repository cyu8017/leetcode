// LeetCode 3173 - Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

object Solution {
  def orArray(nums: Array[Int]): Array[Int] = {
    val ans = new Array[Int](nums.length - 1)
    var i = 1
    while (i < nums.length) {
      ans(i - 1) = nums(i) | nums(i - 1)
      i += 1
    }
    ans
  }
}
