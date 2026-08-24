// LeetCode 3151 - Special Array I
// https://leetcode.com/problems/special-array-i/

object Solution {
  def isArraySpecial(nums: Array[Int]): Boolean = {
    var i = 1
    while (i < nums.length) {
      if (nums(i) % 2 == nums(i - 1) % 2) return false
      i += 1
    }
    true
  }
}
